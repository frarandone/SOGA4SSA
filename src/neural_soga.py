import torch
from torch import nn
import torch.distributions as distr

### Truncation Network

POS = 10**(-3)

class ApproxTruncation(nn.Module):
    def __init__(self, xdim, num_component_input=2, num_component_output=2, nsamples=500):
        super(ApproxTruncation, self).__init__()
        self.num_component_input = num_component_input
        self.num_component_output = num_component_output
        
        self.xdim = xdim
        self.out_dim = self.num_component_output*(1+self.xdim+self.xdim**2)

        self.network = nn.Sequential(
            nn.Linear(self.xdim, 24),
            nn.LeakyReLU(0.2),
            nn.Linear(24, 48),
            nn.LeakyReLU(0.2),
            nn.Linear(48, 48),
            nn.LeakyReLU(0.2),
            nn.Linear(48,24),
            nn.LeakyReLU(0.2),
            nn.Linear(24, self.out_dim),
        )

        self.lay = nn.Linear(nsamples, 1)

    def forward(self, samples):

        output = self.network(samples)

        fl_output = self.lay(output.t())

        fl_output = fl_output.reshape((self.num_component_output,-1))

        weights = torch.sigmoid(fl_output[:, 0])
        weights = weights / weights.sum()
        mus = torch.relu(fl_output[:, 1:self.xdim+1])
        sigmas = 10*torch.tanh(fl_output[:, self.xdim+1:].reshape((self.num_component_output, self.xdim, self.xdim)))

        covs = torch.empty_like(sigmas)
        for i in range(self.num_component_output):
          #covs[i] = torch.mm(sigmas[i],sigmas[i].t())+self.xdim * torch.eye(self.xdim)
          covs[i] = torch.mm(sigmas[i],sigmas[i].t()) + POS*torch.eye(self.xdim)

        return weights, mus, covs

def generate_random_covariance(dim, lb, ub):
    A = torch.empty(dim, dim).uniform_(lb, ub)
    cov_matrix = torch.mm(A, A.t())  # Make it symmetric and semi-definite
    #cov_matrix += dim * torch.eye(dim)  # Make it positive definite
    cov_matrix += torch.rand(1)*torch.eye(dim)  # Make it positive definite

    return cov_matrix

def _truncate_samples(samples, dist):
    # Iteratively resample until all values are positive
    while torch.any(samples[:, 0] < 0):
        negative_indices = torch.where(samples[:,0] < 0)[0]
        new_samples = dist.sample((len(negative_indices),))
        samples[negative_indices] = new_samples
    return samples

def gm_sampling(pis, mus, sigmas, num_samples):
    gm_distributions = [distr.MultivariateNormal(mus[i], sigmas[i]) for i in range(len(pis))]
    component_choices = torch.multinomial(pis, num_samples, replacement=True)
    samples = torch.zeros(num_samples, mus.shape[1])
    for i in range(len(pis)):
        mask = (component_choices == i)
        num_samples_i = mask.sum()
        if num_samples_i > 0:
            tsamples = gm_distributions[i].sample((num_samples_i,))
            samples[mask] = _truncate_samples(tsamples, gm_distributions[i])
            #samples[mask] = gm_distributions[i].sample((num_samples_i,))
    return samples

### Poisson Network

class PoissonNetwork(nn.Module):
    def __init__(self, input_size=6, num_component_output=2):
        super(PoissonNetwork, self).__init__()
        self.input_size = input_size
        self.num_component_output = num_component_output
        self.flatten = nn.Flatten()
        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128,6)
        )

    def forward(self, x):
        output = self.network(x)
        pi = output[:, 0:self.num_component_output]
        mu = output[:, self.num_component_output:2*self.num_component_output]
        sigma = output[:, 2*self.num_component_output:3*self.num_component_output]

        pi = torch.softmax(pi, dim=1)
        sigma = torch.exp(sigma)
        mu = torch.exp(mu)

        return mu, pi, sigma

def generate_poisson(pi, mu, sigma, end = 50):
    """
    Input:
    pi = tensor of weights of length c
    mu = tensor of means of length c
    sigma = tensor of variances of length c
    Taken as input the parameters of a Gaussian Mixtures returns the
    density of a Poisson distribution having as rate given mixture, truncated to [0, end]
    """
    c = len(pi)   # number of components in the mixture
    
    # initializes the density vector, storing a density for each component
    pois_dens = torch.zeros((c, end))
    # initializes the vector of factorials
    log_fact = torch.tensor([sum([torch.log(torch.tensor(float(i))) for i in range(1, n)]) for n in range(1, end+1)])
    
    # computes the Gaussian density for each component
    muprime = mu - sigma
    std = torch.sqrt(sigma)
    norm = distr.normal.Normal(torch.tensor(0.0), torch.tensor(1.0))

    for i in range(c):
        for k_val in range(end):
            if k_val == 0:
                pois_dens[i, k_val] = 1 - norm.cdf(-muprime[i]/std[i])
            elif k_val == 1:
                pois_dens[i, k_val] = muprime[i] * pois_dens[i, k_val-1] + std[i] * norm.log_prob(-muprime[i]/std[i]).exp()
            else:
                pois_dens[i, k_val] = (muprime[i] * pois_dens[i, k_val-1] + (k_val-1) * sigma[i] * pois_dens[i, k_val-2])
        # goes to logarithm to compute the factorial
        pois_dens[i, :] = torch.log(pois_dens[i, :]) - log_fact
        pois_dens[i, :] = pois_dens[i, :].exp()
        # multiplies by normalization constant
        pois_dens[i, :] = pois_dens[i, :] * torch.exp(0.5 * (sigma[i] - 2 * mu[i]))
        # puts missing probability mass to zero
        pois_dens[i, 0] += 1 - pois_dens[i, :].sum()

    # compute product between weights and densities per component
    pois_dens = pi.reshape(1, c).matmul(pois_dens).reshape(end, )
    return pois_dens
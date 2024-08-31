from libSOGAshared import *
from libSOGAtruncate import partitionfunc
from libSOGAupdate import poisson_var

import torch
from torch import nn
from neural_soga import *


def compute_firings(args, dist, data):
    
    # args is in form 'n_rates, [bound_1, ..., bound_m]'
    m = int(args.split(',')[0])
    bounds = (args.split('['))[1].split(']')[0].split(',')
    bounds = [int(bound) for bound in bounds]
       
    rate_idx = []
    for var in dist.var_list:
        if 'rate' in var:
            rate_idx.append(dist.var_list.index(var))
    mu_rate = dist.gm.mu[0][rate_idx]
    sigma_rate = dist.gm.sigma[0][rate_idx, :][:, rate_idx]
    
    if abs(np.linalg.det(sigma_rate)) <= delta_tol:
        # compute k_i as before
        for i in range(m):
            idx = dist.var_list.index('k{}'.format(i+1))
            pois_mu = mu_rate[i]
            pois_sigma = sigma_rate[i][i]
            supp = bounds[i]
            par = 'mom1'
            _, pois_mu, pois_sigma = poisson_var(pois_mu, pois_sigma, supp, var)
            dist.gm.mu[0][idx] = pois_mu[0]
            dist.gm.sigma[0][idx,idx] = pois_sigma[0]
        
    else:
        
        # compute the joint over number of firings
        
        # using rate conditioned to mean state
        #state_idx = []
        #for var in dist.var_list:
        #    if 'state' in var:
        #        state_idx.append(dist.var_list.index(var))
        #sigma_state = dist.gm.sigma[0][state_idx, :][:, state_idx]
        #sigma_rate_state = dist.gm.sigma[0][rate_idx, :][:, state_idx]
        #print('sigma_state', sigma_state)
        #print('sigma_rate_state', sigma_rate_state)
        #
        #sigma_rate = sigma_rate - sigma_rate_state.dot(np.linalg.inv(sigma_state)).dot(np.transpose(sigma_rate_state))
        #print('sigma_rate', sigma_rate)
        
        # first evaluates the integrals
        mu_prime = mu_rate - sigma_rate.dot(np.ones(m))
        K_grid = compute_K_grid(m, bounds, mu_prime, sigma_rate)    # K_grid stores the computation of the integrals
                
        # compute density
        const = np.e**(0.5*np.reshape(-np.ones(m), (1,m)).dot(sigma_rate).dot(np.reshape(-np.ones(m), (m,1)))-np.ones(m).dot(mu_rate))
        const = const[0,0]
        P_grid = {}                                                 # P_grid stores the densities
        tot = 0
        for key, value in K_grid.items():
            P_grid[key] = (1/np.prod([factorial(k) for k in key]))*const*K_grid[key]
            tot = tot + P_grid[key]
        print('tot', tot)
        # missing probability mass moved to (0,0)
        k = tuple([0 for i in range(m)])
        P_grid[k] = P_grid[k] + (1-tot)
           
        
        
        # compute means
        k_mean = np.zeros(m)
        for key, value in K_grid.items():
            k_mean = k_mean + np.array(key).astype(float)*P_grid[key] 
        for i in range(m):
            idx = dist.var_list.index('k{}'.format(i+1))
            dist.gm.mu[0][idx] = k_mean[i]
            
        # compute second moments
        for i in range(m):
            for j in range(i+1):
                mom = 0
                idxi = dist.var_list.index('k{}'.format(i+1))
                idxj = dist.var_list.index('k{}'.format(j+1))
                for key, value in K_grid.items():
                    mom = mom + key[i]*key[j]*P_grid[key] 
                mom = mom - k_mean[i]*k_mean[j]
                dist.gm.sigma[0][idxi, idxj] = dist.gm.sigma[0][idxj,idxi] = mom
                
        idx_list = []
        for var in ['k1', 'k2']:
            idx_list.append(dist.var_list.index(var))
        print('mean:', dist.gm.mu[0][idx_list])
        print('cov:\n', dist.gm.sigma[0][idx_list,:][:,idx_list])   
                        
    return dist


def compute_K_grid(m, bounds, mu_prime, sigma_rate):
    
    K_grid = {}
    
    # if one dimensional no recursion
    if m == 1:
        for b in range(bounds[0]):
            if b == 0:
                K_grid[(b,)] = 1 - norm.cdf(-mu_prime[0]/sigma_rate[0,0])
            elif b == 1:
                K_grid[(b,)] = mu_prime[0]*K_grid[(0,)] + np.sqrt(sigma_rate[0,0])*norm.pdf(-mu_prime[0]/sigma_rate[0,0])
            else:
                K_grid[(b,)] = mu_prime[0]*K_grid[(b-1,)] + (b-1)*sigma_rate[0,0]*K_grid[(b-2,)]
        return K_grid
        
    # if m > 1 recursion    
    id_matrix = np.eye(m)
    # computing for zero
    k = tuple([0 for i in range(m)])
    K_grid[k] = zeroK(mu_prime, sigma_rate)
    k_queue = [k]
    
    # for each element k in the queue we compute the moments for k+ei and push k+ei in the queue
    while(len(k_queue)>0):
        k = k_queue.pop(0)
        for i in range(m):
            ei = id_matrix[i, :].astype(int)
            # if still in the bounds and not already computed computes the moment k + ei
            if all(bounds - np.array(k + ei) > 0) and not (tuple(k + ei) in K_grid.keys()):
                K_grid = computeK(k, ei, i, mu_prime, sigma_rate, K_grid)
                k_queue.append(k+ei)
    return K_grid
    

def computeK(k, ei, i, mu, sigma, K_grid):
    # computes the recurrence relation for k+ei
    d = np.zeros(len(mu))
    for j in range(len(d)):
        if k[j]  > 0:
            ej = np.zeros(len(k))
            ej[j] = 1
            d[j] = k[j]*K_grid[tuple(k - ej)]
        else:
            if sigma[j,j] == 0:
                # I am adding this correction arbitrarily
                d[j] = 0
            else:
                mu_tilde = np.delete(mu, j) - np.delete(sigma, j, axis=0)[:,j]*(mu[j]/sigma[j,j])
                sigma_tilde = np.delete(np.delete(sigma, j, axis=0), j, axis=1) - (1/sigma[j,j])*np.reshape(np.delete(sigma, j, axis=0)[:,j], (len(sigma)-1,1)).dot(np.reshape(np.delete(sigma,j, axis=1)[j,:], (1, len(sigma)-1)))
                small_bounds = (np.delete(k, j) + np.ones(len(k)-1)).astype(int)
                small_K_grid = compute_K_grid(len(mu_tilde), small_bounds, mu_tilde, sigma_tilde) 
                d[j] = norm.pdf(0, loc=mu[j], scale=np.sqrt(sigma[j,j]))*small_K_grid[tuple(np.delete(k, j).astype(int))]
            
    res = mu[i]*K_grid[tuple(k)] + sum([sigma[i,j]*d[j] for j in range(len(k))])
    
    K_grid[tuple(k+ei)] = res
    
    return K_grid




def zeroK(mu, sigma):
    """
    Computes the mass probability of the normal distribution with mean mu and covariance matrix sigma in the 
    hyper-rectangle [0,infty].
    """
    n = len(mu)
    P = 0
    for i_list in product(*[[0,1]]*n):
        x = np.zeros(n)
        for i, idx in enumerate(i_list):
            if idx==0:
                x[i] = 0
            else:
                x[i] = np.inf
        try:
            p = mvnorm.cdf(x,mean=mu,cov=sigma,allow_singular=True)
        except ValueError:
            sigma = make_psd(sigma)
            p = mvnorm.cdf(x,mean=mu,cov=sigma,allow_singular=True)
        if np.isnan(p):
            # due to a bug in scipy (https://github.com/scipy/scipy/issues/7669), when applied to two dimensional vectors mvnorm.cdf can return nan. The problem is solvable by adding a third variable, indipendent from the others (does not affect the computed probability).
            new_x = list(x) + [0]
            new_mu = list(mu) + [0]
            new_sigma = list(sigma)
            for i in range(len(sigma)):
                new_sigma[i] = list(sigma[i]) + [0]
            new_sigma.append([0]*(len(sigma)+1))
            p = mvnorm.cdf(new_x, mean=new_mu, cov=new_sigma, allow_singular=True)
        P = P + ((-1)**(n-sum(i_list)))*p
    return P

### Truncating state Xnext with neural network

def truncate_state(dist):
    # uses a neural network to perform truncation Xnext>=0
    ncomp = 1
    xdim = 2
    nsamples = 500
    model = ApproxTruncation(xdim, ncomp, ncomp, nsamples)
    model = torch.load('params/truncNNdim2-1to1.pth')
    var_idx = [i for i in range(len(dist.var_list)) if 'Xnext[' in dist.var_list[i]]
    Xnext_mean = torch.tensor(dist.gm.mu[0][var_idx])
    Xnext_cov = torch.tensor(dist.gm.sigma[0][var_idx, :][:, var_idx] + 1e-10*np.eye(2)) # I had to ensure positive definedness for torch
    #print('initial mean', Xnext_mean, 'initial std', Xnext_cov)
    samples = distr.MultivariateNormal(Xnext_mean, Xnext_cov).sample((500,))
    pi_pred, mu_pred, sigma_pred = model(samples.float())
    #print('pred:', mu_pred, sigma_pred)
    for i in range(ncomp):
        Xnext_pred_mean = mu_pred.detach().numpy()[0][i]
        Xnext_pred_cov = sigma_pred.detach().numpy()[0][0][i]
        print(Xnext_pred_mean, Xnext_pred_cov)
        dist.gm.mu[i][var_idx] = Xnext_pred_mean
        dist.gm.sigma[i][var_idx,:][:,var_idx] = Xnext_pred_cov 
    return dist
# Contains the functions for computing the resulting distribution when an assignment instruction is encountered (in state nodes).

# SOGA (defined in SOGA.py)
# |- update_rule
#    |- sym_expr
#    |- update_gaussian

from libSOGAshared import *
from ASGMTListener import *
from ASGMTParser import * 
from ASGMTLexer import *
import torch
from torch import nn
from neural_soga import *

from libSOGAmerge import *

def poisson_prune(pois_pi, pois_mu, pois_sigma):
    pois_mu = [np.array(mu) for mu in pois_mu]
    pois_sigma = [np.array(sigma) for sigma in pois_sigma]
    rate_dist = Dist(['rate'], GaussianMix(pois_pi, pois_mu, pois_sigma))
    rate_dist = prune(rate_dist, 'ranking', 2)
    return rate_dist.gm.pi, rate_dist.gm.mu, rate_dist.gm.sigma


def correct_sigma_rate(pvar, comp):
    
    # conditioning to rates
    
    target = comp.var_list[pvar]
    n_react = sum([1 for var in comp.var_list if 'rate' in var])
    rate_idx = []
    for i in range(1,n_react+1):
        if 'rate{}'.format(i) != target:
            rate_idx.append(comp.var_list.index('rate{}'.format(i)))
            
    sig = comp.gm.sigma[0][pvar,pvar]
    sig12 = comp.gm.sigma[0][pvar][rate_idx]
    sig21 = np.transpose(sig12)
    sig22 = comp.gm.sigma[0][rate_idx][:,rate_idx]
    
    if np.linalg.det(sig22) > delta_tol:
        corr_sig = sig - sig12.dot(np.linalg.inv(sig22)).dot(sig21)
        if corr_sig > delta_tol:
            #print('returning', corr_sig, 'instead of', sig, 'mean', comp.gm.mu[0][pvar])
            return sig - sig12.dot(np.linalg.inv(sig22)).dot(sig21)
        else:
            #print('returning', 0, 'instead of', sig, 'mean', comp.gm.mu[0][pvar])
            return 0
    else:
        return sig
   
    # conditioning to state
    
    #target = comp.var_list[pvar]
    #n_species = sum([1 for var in comp.var_list if 'state' in var])
    #state_idx = []
    #for i in range(0,n_species):
    #    state_idx.append(comp.var_list.index('state[{}]'.format(i)))
    #        
    #sig = comp.gm.sigma[0][pvar,pvar]
    #sig12 = comp.gm.sigma[0][pvar][state_idx]
    #sig21 = np.transpose(sig12)
    #sig22 = comp.gm.sigma[0][state_idx][:,state_idx]
    #
    #if np.linalg.det(sig22) > 0:
    #    corr_sig = sig - sig12.dot(np.linalg.inv(sig22)).dot(sig21)
    #    if corr_sig > delta_tol:
    #        print('returning', corr_sig, 'instead of', sig, 'mean', comp.gm.mu[0][pvar])
    #        return corr_sig
    #    else:
    #        print('returning', 0, 'instead of', sig, 'mean', comp.gm.mu[0][pvar])
    #        return 0
    #else:
    #    print('no correction')
    #    return sig


def poisson_var(pois_mu, pois_sigma, supp, par):
    """ Approximates a Pois(N(pois_mu, pois_sigma)) (pois_sigma is the variance) variable with a N(mu, sigma) variable """ 
    pois_it = np.zeros(supp)
    pois_sigma = np.sqrt(pois_sigma)
    muprime = pois_mu - pois_sigma**2
    # if rate is non-positive and variable is a delta
    if pois_sigma == 0. and pois_mu <= 0:
        return [1.], [0.], [0.]
    # if variable is a delta
    elif pois_sigma < delta_tol: 
        return [1.], [pois_mu], [pois_mu]
    # all other cases
    #pois_mu, pois_var = truncnorm.stats(-pois_mu/pois_sigma, np.inf, pois_mu, pois_sigma) 
    #pois_sigma = np.sqrt(pois_var)
    for k_val in range(supp):
        if k_val ==0:
            pois_it[k_val] = 1 - norm.cdf(-muprime/pois_sigma)
        elif k_val == 1:
            pois_it[k_val] = muprime*pois_it[k_val-1] + pois_sigma*norm.pdf(-muprime/pois_sigma)
        else:
            pois_it[k_val] = (muprime*pois_it[k_val-1] + (k_val-1)*(pois_sigma**2)*pois_it[k_val-2])
    #print('pois_it', pois_it, 'log(pois_it)', np.log(pois_it))
    log_fact = np.array([sum([np.log(i) for i in range(1,n)]) for n in range(1,supp+1)])
    pois_it = np.log(pois_it) - log_fact
    pois_it = np.exp(pois_it)
    #pois_it = pois_it/sum(pois_it)
    pois_it = pois_it*np.exp(0.5*(pois_sigma**2-2*pois_mu))
    pois_it[0] += 1 - sum(pois_it)
    if par == 'disc':
        return pois_it, range(supp), np.zeros(supp)
    elif par == 'mom1':
        print('input', pois_mu, pois_sigma)
        model = PoissonNetwork(input_size=supp, num_component_output=1)
        model = torch.load('params/poisson_dim1.pth')
        mu_new, pi_new, sigma_new = model(torch.tensor(pois_it).reshape(1,50).double())
        mu_new = mu_new.detach().numpy()
        sigma_new = sigma_new.detach().numpy()
        print('fit with neural network', mu_new, sigma_new, sigma_new**2)
        mean = np.array(range(supp)).dot(pois_it)
        var = (np.array(range(supp))**2).dot(pois_it)-mean**2
        print('analytical fit', mean, var)
        return [1.], [mean], [var]
    else:
        return [1.], [pois_mu], [pois_sigma]


class AsgmtRule(ASGMTListener):
    
    def __init__(self, var_list, data):
        self.var_list = var_list
        self.data = data
        self.func = None           # stores the function
        self.target = None         # stores the index of the target variable
        self.comp_flag = True      # if True updates the distribution component by component
        
        self.aux_pis = []          # stores the weights of auxiliary variables
        self.aux_means = []        # stores the means of auxiliary variables
        self.aux_covs = []         # stores the cov matrices of auxiliary variables
        
        self.pois_idx = []         # stores indices of poisson variables
        self.pois_vars = []        # stores poisson terms depending on variables
        
        self.is_prod = None        # checks whether a term is a product of two vars
        
    def process_poisson(self, poisson):
        """ depending on the parameters in the poisson, saves it using different representations """
        prate, psupp, ppar = poisson.prate(), poisson.psupp(), poisson.ppar()
        # CASE 1: rate is a number
        if not prate.NUM() is None:
            rate = float(prate.getText())
            supp = int(psupp.getText())
            if ppar.getText() == 'disc':
                self.aux_pis.append([pois.pmf(k, rate) for k in range(supp)])
                self.aux_means.append(list(range(supp)))
                self.aux_covs.append(list(np.zeros(supp)))
            elif ppar.getText() == 'nbin':
                pass
            elif ppar.getText() == 'mom1':
                mu, var = truncnorm.stats(-np.sqrt(rate), np.inf, rate, np.sqrt(rate))
                self.aux_pis.append([1.])
                self.aux_means.append([mu])
                self.aux_covs.append([np.sqrt(var)])
            elif ppar.getText() == 'mom2':
                pass
        # CASE 2: rate is a variable
        else:
            # fitting with discrete or one Gaussian
            if ppar.getText() == 'disc' or ppar.getText() == 'mom1':
                # put placeholders in aux_pis, aux_means, aux_covs
                self.aux_pis.append([None])
                self.aux_means.append([None])
                self.aux_covs.append([None])
                rate = prate.symvars().getVar(self.data)
                var_idx = self.var_list.index(rate)
                supp = int(psupp.getText())
                self.pois_vars.append((var_idx, supp, ppar.getText()))
            elif ppar.getText() == 'mom2':
                # fitting with two Gaussian
                self.comp_flag = False
                rate = prate.symvars().getVar(self.data)
                var_idx = self.var_list.index(rate)
                
                def mom2_func(dist):
                                        
                    pois_pi = dist.gm.pi
                    pois_mu = [mean[var_idx] for mean in dist.gm.mu]
                    pois_sigma = [sigma[var_idx, var_idx] for sigma in dist.gm.sigma]
                                        
                    model = NeuralNetwork(2, 2)
                    model = torch.load('model3.pth')
                    if(len(pois_pi) < 2):
                        pois_pi = pois_pi + [0.0]
                        pois_mu = np.array(pois_mu + [0.0])
                        pois_sigma = np.array(pois_sigma + [0.0])
                        
                    if (len(pois_pi) > 2):
                        pois_pi, pois_mu, pois_sigma = poisson_prune(pois_pi, pois_mu, pois_sigma)
                                                
                    mu_new, pi_new, sigma_new = model(torch.cat((torch.tensor(pois_pi).type(torch.float32),torch.tensor(pois_mu).type(torch.float32),torch.tensor(pois_sigma).type(torch.float32)), dim=0).reshape(1,6))

                    pi_new = pi_new.detach().numpy().flatten()
                    mu_new = mu_new.detach().numpy().flatten()
                    sigma_new = sigma_new.detach().numpy().flatten()
                    
                    final_pi = []
                    final_mu = []
                    final_sigma = []
                    for k in range(dist.gm.n_comp()):
                        final_pi += list(dist.gm.pi[k]*pi_new)
                        mu1, mu2 = copy(dist.gm.mu[k]), copy(dist.gm.mu[k])
                        mu1[self.target] = mu_new[0]
                        mu2[self.target] = mu_new[1]
                        final_mu += [mu1, mu2]
                        sigma1, sigma2 = copy(dist.gm.sigma[k]), copy(dist.gm.sigma[k])
                        sigma1[self.target, self.target] = sigma_new[0]
                        sigma2[self.target, self.target] = sigma_new[1]
                        final_sigma += [sigma1, sigma2]
                    
                    return GaussianMix(final_pi, final_mu, final_sigma)
                
                self.func = mom2_func
                
        
    def enterAssignment(self, ctx):
        self.target = self.var_list.index(ctx.symvars().getVar(self.data))
   
       
    def enterAdd(self, ctx):
        
        if len(ctx.add_term())==1 and len(ctx.add_term(0).term()) == 2:
            self.is_prod = 1
            for term in ctx.add_term(0).term():
                self.is_prod = self.is_prod*term.is_var(self.data)
        if self.is_prod:
            self.mul_idx = []
        else:
            self.add_coeff = [0.]*len(self.var_list)
            self.add_const = 0
            
            
    def enterAdd_term(self,ctx):
        # product between variables
        if self.is_prod:
            
            for term in ctx.term():
                if not term.gm() is None:
                    self.aux_pis.append(eval(term.gm().list_()[0].getText()))
                    self.aux_means.append(eval(term.gm().list_()[1].getText()))
                    self.aux_covs.append(np.array(eval(term.gm().list_()[2].getText()))**2)
                    self.mul_idx.append(int(len(self.var_list)+len(self.aux_pis)-1))
                elif not term.symvars() is None:
                    self.mul_idx.append(self.var_list.index(term.symvars().getVar(self.data)))
            
            
            def mul_func(comp):
                i = self.target
                j, k = self.mul_idx
                mu = comp.gm.mu[0]
                sigma = comp.gm.sigma[0]
                final_pi = []
                final_mu = []
                final_sigma = []
                for part in product(*[range(len(mean)) for mean in self.aux_means]):
                    # STEP 1: for a given combination of components of the auxiliary variables, creates a new component extending comp
                    aux_pi = 1
                    aux_mean = list(copy(mu))
                    aux_sigma = []
                    for p,q in zip(range(len(self.aux_means)), part):
                        aux_pi = aux_pi*self.aux_pis[p][q]
                        aux_mean.append(self.aux_means[p][q])
                        aux_sigma.append(self.aux_covs[p][q])
                    aux_mean = np.array(aux_mean)
                    aux_sigma = np.diag(aux_sigma)
                    aux_cov = np.block([[sigma, np.zeros((len(sigma), len(aux_sigma)))], [np.zeros((len(aux_sigma), len(sigma))), aux_sigma]])
                    # STEP 2: computes mean and covariance matrix for the extended component
                    new_mu = copy(mu)
                    new_mu[i] = (aux_cov[j,k] + aux_mean[j]*aux_mean[k])
                    new_sigma = copy(sigma)
                    new_sigma[i,:] = new_sigma[:,i] = (aux_mean[j]*aux_cov[k,:] + aux_mean[k]*aux_cov[j,:])[:len(mu)] 
                    new_sigma[i,i] = (aux_cov[j,k]**2 + 2*aux_cov[j,k]*aux_mean[j]*aux_mean[k] + aux_cov[j,j]*aux_cov[k,k] + aux_cov[j,j]*aux_mean[k]**2 + aux_cov[k,k]*aux_mean[j]**2)
                    # STEP 3: appends weight, new mean and new covariance matrix to the final vectors
                    final_pi.append(aux_pi)
                    final_mu.append(new_mu)
                    final_sigma.append(new_sigma)
                    
                return GaussianMix(final_pi, final_mu, final_sigma)
                        
            self.func = mul_func
        
        # linear combination
        else:
            coeff = 1
            var_idx = None
            for term in ctx.term():
                if term.sub() is not None:
                    coeff = -1*coeff
                else:
                    coeff = 1*coeff
                # determines the kind of term is appearing in the sum
                # constant
                if term.is_const(self.data):
                    coeff = coeff*term.getValue(self.data)
                # symbolic variable (saves the index in var_idx) 
                elif not term.symvars() is None:
                    var_idx = self.var_list.index(term.symvars().getVar(self.data))
                # gm (extends the distribution with auxiliary variables)
                elif not term.gm() is None:
                    self.aux_pis.append(eval(term.gm().list_()[0].getText()))
                    self.aux_means.append(eval(term.gm().list_()[1].getText()))
                    self.aux_covs.append(np.array(eval(term.gm().list_()[2].getText()))**2)
                    var_idx = len(self.add_coeff) + 1
                # poisson (extends the distribution with auxiliary variables)
                elif not term.poisson() is None:
                    self.process_poisson(term.poisson())
                    var_idx = len(self.add_coeff) + 1
                    self.pois_idx.append(var_idx)
            if not var_idx is None:
                if var_idx < len(self.add_coeff):
                    self.add_coeff[var_idx] = coeff
                else:
                    self.add_coeff.append(coeff)
            else:
                self.add_const = self.add_const + coeff
                                
    def exitAdd(self, ctx):
        if not self.is_prod:
            if not np.all(np.array(self.add_coeff) == 0):
                
                def add_func(comp):
                    i = self.target
                    mu = comp.gm.mu[0]
                    sigma = comp.gm.sigma[0]
                    final_pi = []
                    final_mu = []
                    final_sigma = []
                    
                    # computes the auxiliary variables deriving from poisson terms
                    if len(self.pois_idx) > 0:
                        self.pois_idx.reverse()
                        self.pois_vars.reverse()
                        for pidx, pvar in enumerate(self.pois_vars):
                            # extracts stats
                            pois_mu = mu[pvar[0]]
                            pois_sigma = sigma[pvar[0],pvar[0]]  # is the variance
                            #pois_sigma = correct_sigma_rate(pvar[0], comp)
                            supp = pvar[1]
                            par = pvar[2]
                            
                            # computes representation of poisson
                            pois_pi, pois_mean, pois_cov = poisson_var(pois_mu, pois_sigma, supp, par)
                          
                            # extends vector of auxiliary variables
                            idx = self.pois_idx[pidx] - len(mu)
                            self.aux_pis = self.aux_pis[:idx-1] + [pois_pi] + self.aux_pis[idx:]
                            self.aux_means = self.aux_means[:idx-1] + [pois_mean] + self.aux_means[idx:]
                            self.aux_covs = self.aux_covs[:idx-1] + [pois_cov] + self.aux_covs[idx:]

                    #computes extended component with auxialiary variables
                    for part in product(*[range(len(mean)) for mean in self.aux_means]):
                        aux_pi = 1
                        aux_mean = list(copy(mu))
                        aux_sigma = []
                        for p,q in zip(range(len(self.aux_means)), part):
                            aux_pi = aux_pi*self.aux_pis[p][q]
                            aux_mean.append(self.aux_means[p][q])
                            aux_sigma.append(self.aux_covs[p][q])
                        aux_mean = np.array(aux_mean)
                        aux_sigma = np.diag(aux_sigma)
                        aux_cov = np.block([[sigma, np.zeros((len(sigma), len(aux_sigma)))], [np.zeros((len(aux_sigma), len(sigma))), aux_sigma]])
                        # computes mean and covariance matrix for the extended component
                        # implementation 1
                        #A = np.eye(len(aux_mean)) 
                        #A[i,:] = np.array(self.add_coeff)
                        #b = np.zeros(len(aux_mean))
                        #b[i] = self.add_const
                        #new_mu = A.dot(aux_mean) + b
                        #new_mu = new_mu[:len(mu)]
                        #new_sigma = A.dot(aux_cov).dot(np.transpose(A))
                        #new_sigma = new_sigma[:len(mu),:len(mu)]
                        # implementation 2
                        new_mu = copy(mu)
                        new_mu[i] = np.array(self.add_coeff).dot(aux_mean) + np.array(self.add_const)
                        new_sigma = copy(sigma)
                        new_sigma[i,:] = new_sigma[:,i] = np.array(self.add_coeff).dot(aux_cov)[:len(mu)]
                        new_sigma[i,i] = np.array(self.add_coeff).dot(aux_cov).dot(np.array(self.add_coeff))
                        # STEP 3: appends weight, new mean and new covariance matrix to the final vectors
                        final_pi.append(aux_pi)
                        final_mu.append(new_mu)
                        final_sigma.append(new_sigma)
                    return GaussianMix(final_pi, final_mu, final_sigma)
                
                if self.func is None:
                    self.func = add_func
            
            else:
                
                c = self.add_const
                
                def const_func(comp):
                    i = self.target
                    new_mu = copy(comp.gm.mu[0])
                    new_sigma = copy(comp.gm.sigma[0])
                    new_mu[i] = c
                    new_sigma[i,:] = np.zeros(len(new_mu))
                    new_sigma[:,i] = np.zeros(len(new_mu))
                    return GaussianMix(comp.gm.pi, [new_mu], [new_sigma])
                
                if self.func is None:
                    self.func = const_func
        
    
def asgmt_parse(var_list, expr, data):
    """ Parses expr using ANTLR4. Returns a function """
    lexer = ASGMTLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = ASGMTParser(stream)
    tree = parser.assignment()
    asgmt_rule = AsgmtRule(var_list, data)
    walker = ParseTreeWalker()
    walker.walk(asgmt_rule, tree) 
    return asgmt_rule.func, asgmt_rule.comp_flag
        
        
def update_rule(dist, expr, data):
    """ Applies expr to dist. It first parses expr using the function asgmt_parse, implemented as an ANTLR listener. asgmt_parse returns a function rule_func, such that, rule_func(GaussianMix) returns a new GaussianMix object obtained applying expr to the initial distribution. rule_func is applied to each component of dist, and the resulting Gaussian mixtures are stored in a single GaussianMix object."""
    
    if expr == 'skip':
        return dist
    else:
        rule_func, comp_flag = asgmt_parse(dist.var_list, expr, data)    # define function
        new_pi = []
        new_mu = []
        new_sigma = []
        if comp_flag: 
            for k in range(dist.gm.n_comp()):
                comp = Dist(dist.var_list, dist.gm.comp(k))
                new_mix = rule_func(comp)
                new_pi += list(dist.gm.pi[k]*np.array(new_mix.pi))
                new_mu += new_mix.mu
                new_sigma += new_mix.sigma
            return Dist(dist.var_list, GaussianMix(new_pi, new_mu, new_sigma))
        else:
            return Dist(dist.var_list, rule_func(dist))
            
        
    
    


    
    
    
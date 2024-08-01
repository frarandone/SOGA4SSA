import numpy as np

def next_reaction(drift, S, c, X0, T, steps=500):
    """
    drift: list of rate functions
    S: Stoichiometry matrix. Each row represents a reaction, and each column represents a species.
    c: Array of reaction rates.
    X0: Initial state.
    T: Total time.
    """
    t_ssa = np.linspace(0,T,steps)
    X_ssa = []
    
    X = []
    t = []
    t_now = 0.
    X.append(X0)
    t.append(t_now)

    while t_now < T:
        # Calculate propensities
        a = c * np.array([rate(X[-1]) for rate in drift])

        # Generate exponentially distributed random variables
        rand_vars = np.random.exponential(1 / a)

        # Find the index of the next reaction
        next_reaction_idx = np.argmin(rand_vars)

        # Find the time until the next reaction
        tau = rand_vars[next_reaction_idx]

        # Update time and state
        t_now += tau
        X_now = X[-1] + S[next_reaction_idx, :]

        # Ensure time does not exceed total time
        if t_now > T:
            t_now = T
            X.append(X_now)
            t.append(t_now)
            break

        # Update state and time
        X.append(X_now)
        t.append(t_now)
        
    X_ssa.append(X0)
    for j in range(1,len(t_ssa)):
        for i in range(len(t)-1):
            if t[i+1] < t_ssa[j]:
                continue
            else:
                X_ssa.append(X[i])
                break
    
    return np.array(X_ssa), np.array(t_ssa)


def tau_leaping(drift, S, c, X0, T, tau, returnK=False):
    """
    drift: list of rate functions
    S: Stoichiometry matrix. Each row represents a reaction, and each column represents a species.
    c: Array of reaction rates.
    X0: Initial state.
    T: Total time.
    tau: Leap size.
    """
    steps = int(np.ceil(T/tau))
    X = []
    t = []
    K_list = []
    t0 = 0.
    X.append(X0)
    t.append(t0)
    
    for j in range(steps):
        a = c*np.array([rate(X[j]) for rate in drift])  # Propensity function
        K = np.random.poisson(a*tau)  # Number of reactions
        K_list.append(K)
        X_new = X[j] + np.dot(K, S)  # Update the state
        X.append(X_new)
        t.append(t[j]+tau)

        # Check for negative populations
        if np.any(X[j+1] < 0):
            print('Negative population, restarting run')
            return None, t
    if returnK:
        return X, K_list, t
    else:
        return X, t

def mean_field(drift, S, c, X0, t_axis,size=1):
    dt = t_axis[1] - t_axis[0]
    X = []
    X.append(X0/size)
    i = 0

    for j in range(len(t_axis)-1):
        a = c*np.array([rate(size*X[j]) for rate in drift])  # Propensity function
        X.append(X[j] + np.dot(a*dt,S/size))  # Update the state
    return np.array(X)


def euler_maruyama(drift, S, c, X0, t_axis):
    dt = t_axis[1] - t_axis[0]
    X = []
    X.append(X0)
    i = 0

    for j in range(len(t_axis)-1):
        a = c*np.array([rate(X[j]) for rate in drift])  # Propensity function
        X.append(X[j] + np.dot(a*dt,S) + np.dot(np.sqrt(a*dt)*np.random.normal(0,1,len(drift)),S))  # Update the state
        if np.any(X[j+1] < 0):
            #print('Negative population, restarting run')
            return None
    return np.array(X)

def linear_noise(drift,jac,S,c,X0,t_axis,size=1):
    
    dt = t_axis[1] - t_axis[0]
    X = []
    X.append(X0/size)
    
    Sigma = []
    Sigma0 = np.zeros((len(X0), len(X0)))
    Sigma.append(Sigma0)
    
    def Dfunc(X):
        D = np.zeros((len(X0), len(X0)))
        for i in range(len(X0)):
            for j in range(i,len(X0)):
                D[i,j] = D[j,i] = sum([S[r,i]*S[r,j]*drift[r](size*X) for r in range(len(drift))])
        return D
    
    def Jfunc(X):
        return S.transpose().dot(jac(size*X))
    
    for j in range(len(t_axis)-1):
        a = c*np.array([rate(size*X[j]) for rate in drift])  # Propensity function
        X.append(X[j] + np.dot(a*dt,S/size))  # Update the state
        Sigma.append(Sigma[j] + dt*(Jfunc(X[j]).dot(Sigma[j]) + Sigma[j].dot(Jfunc(X[j]).transpose()) + (1/size)*Dfunc(X[j])))
                     
    return size*np.array(X), size*np.array(Sigma)

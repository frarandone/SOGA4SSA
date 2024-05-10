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
    X_ssa = np.zeros(len(t_ssa))
    
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
        
    X_ssa[0] = X0
    for j in range(1,len(t_ssa)):
        for i in range(len(t)-1):
            if t[i+1] < t_ssa[j]:
                continue
            else:
                X_ssa[j] = X[i]
                break
    
    return np.array(X_ssa), np.array(t_ssa)


def tau_leaping(drift, S, c, X0, T, tau):
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
    t0 = 0.
    X.append(X0)
    t.append(t0)
    
    for j in range(steps):
        a = c*np.array([rate(X[j]) for rate in drift])  # Propensity function
        K = np.random.poisson(a*tau)  # Number of reactions
        X_new = X[j] + np.dot(K, S)  # Update the state
        X.append(X_new)
        t.append(t[j]+tau)

        # Check for negative populations
        if np.any(X[j+1] < 0):
            #print('Negative population, restarting run')
            return None, t

    return X, t

def mean_field(drift, S, c, X0, t_axis):
    dt = t_axis[1] - t_axis[0]
    X = []
    X.append(X0)
    i = 0

    for j in range(len(t_axis)-1):
        a = c*np.array([rate(X[j]) for rate in drift])  # Propensity function
        X.append(X[j] + np.dot(a*dt,S))  # Update the state
    return np.array(X)
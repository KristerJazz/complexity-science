import numpy as np

class Applause:
    def __init__(self, **kwargs):
        """
        Initialize an applause rule with default parameters
        ------
        Parameters:
            a = ;
            b = ;
            alpha = ;
            beta = ;
        """
        self.default = {'a':0.5, 'b':0.3, 'alpha':1, 'beta':5}
        self.update_parameters(**kwargs)

    def update_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self.default[key] = value

        self.a = self.default['a'] 
        self.b = self.default['b']
        self.alpha = self.default['alpha'] 
        self.beta = self.default['beta'] 

    def apply(self, current, neighbors):
        state0 = (current==0)
        state1 = (current==1)
        total1 = np.sum(state1.astype(int))
        total0 = np.sum(state0.astype(int))
        N = current.size-1
        
        p01 = np.ones_like(current)*self.a*self.alpha*total1/N
        p10 = np.ones_like(current)*self.b/(1+(self.beta*(total1/N)))

        mc_die1 = np.random.random(current.shape)
        mc_die2 = np.random.random(current.shape)
        
        p01_result = (p01 > mc_die1)
        p10_result = (p10 > mc_die2)
        
        result1 = np.logical_and(state0, p01_result).astype(int)
        result0 = np.logical_and(state1, p10_result).astype(int)

        result = current-result0

        return result

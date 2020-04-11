import numpy as np

class SIRC_Gillespie:
    def __init__(self, **kwargs):
        """
		S-I-R-C rule
		S - Susceptible
		I - Infectious
        C - Infectious
		R - Recovered
        ---------------
        Parameters

		---------------
		Returns : None
        """

        self.update_matrix = np.zeros([4,4])
        """						S I R C update matrix"""
        self.update_matrix[0] = [-1,1,0,0]
        self.update_matrix[1] = [0,-1,1,0]
        self.update_matrix[2] = [0,-1,0,1] 
        self.update_matrix[3] = [0,0,-1,1] 

        self.default = {'alpha' : 0.17,
                        'beta' : 0.36,
                        'gamma_c' : 0.87,
                        'gamma_i' : 0.03,
                        'q' : 0.1,
                        'update_matrix' : self.update_matrix
                        }

        self.update_parameters(**kwargs)
        self.t = 0

    def update_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self.default[key] = value

        self.alpha = self.default['alpha']
        self.beta = self.default['beta']
        self.gamma_c = self.default['gamma_c']
        self.gamma_i = self.default['gamma_i']
        self.q = self.default['q']
        self.update_matrix = self.default['update_matrix']

    def compute_prob(self, population):
        #simple normalization
        s_i = self.beta*(population[1]/population.sum() + ((1-self.q)*population[2]/population.sum()))*population[0] 
        i_c = self.alpha*population[1]
        i_r = self.gamma_i*population[1]*(1-self.alpha)
        c_r = self.gamma_c*population[2]
        
        p = np.array([s_i, i_c, i_r, c_r])
        return p

    def apply(self, current, adj):
        for i in range(len(current[0])):
            prob = self.compute_prob(current[:,i])
            if prob.sum()==0:
                dt = 100
                pass
            else:
                r = prob/prob.sum()
                choice = np.random.choice([0,1,2,3], p=r)
                current[:,i] = current[:,i]+self.update_matrix[choice]
                dt = (1/prob.sum()) * np.log(1/np.random.random())
        self.t += dt

        return current

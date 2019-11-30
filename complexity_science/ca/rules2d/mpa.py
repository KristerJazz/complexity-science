import numpy as np

class MPA:
    def __init__(self, gammafield, **kwargs):
        """
        Initializes an logistic growth, harvest and diffusion rule to an marine area;
        with protected regions also known as MPAs.
        ---------------
        Parameters
            gammafield = 0: harvest over growth rate ratio (0 means protected areas
                            1 means harvest is proportional to growth)
            beta = 1: harvest method exponent ( beta > 1 means catastrophic harvest method
                       beta < 1 means sustainable harvest method)
            D = 25: diffusion rate
            dt = 0.001: time step
            alpha = D*dt : 
        """
        self.default = {'dt' : 0.01,
                        'beta' : 1,
                        'D' : 25
                        }
        self.default['gammafield'] = gammafield
        self.gammafield = gammafield

        self.update_parameters(**kwargs)

    def update_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self.default[key] = value

        self.dt = self.default['dt']
        self.beta = self.default['beta']
        self.D = self.default['D']
        self.gammafield = self.default['gammafield'] 

        self.alpha = self.D*self.dt 

    def apply(self, current, neighbors):
        #DIFFUSION
        total_neighbors = np.zeros_like(current)
        for key in neighbors:
            total_neighbors += neighbors[key]

        current = current*(1-(4*self.alpha))+self.alpha*total_neighbors

        #GROWTH
        result = current/(current +(1-current)*np.exp(-self.dt))

        #HARVEST
        harvest = self.gammafield*self.dt*np.exp(self.beta*np.log(current))
        result -= harvest
        
        #print(self.gammafield)
        return result

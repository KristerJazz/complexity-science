import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .rule_manager import RuleManager


class CA2D:
    def __init__(self, dim):
        """
        Creates an 2D cellular automata object of a given dimension with random value from 0-1. See related initialize_ functions to initialize properly.
        ---------------
        Parameters:
            dim = cellular automata matrix shape

        Attributes
        n1 = left-top neighbor of new_state
        n2 = top neighbor of new_state
        n3 = right-top neighbor of new_state
        n4 = left neighbor of new_state
        n5 = right neighbor of new_state
        n6 = right-bottom neighbor of new_state
        n7 = bottom neighbor of new_state
        n8 = left-bottom neighbor of new_state
        ---------------
        Returns:
            None
        """
        self.size = dim
        self.cells = np.random.random(dim)
        self.rm = RuleManager()
        #self.dc = DataCollector()
        self.update_neighbors()

    def update_neighbors(self):
        raise NotImplementedError("This is the base class; Please choose a CA with defined neighborhood:\n VON_CA_t, VON_CA, MOORE_CA_t, MOORE_CA")

    def evolve(self):
        """
        Evolves the CA according to the rule applied.
        Updates the state of the cell.
            cell = new_state

        Updates the neighbor according to the new_state
            n1 = left-top neighbor of new_state
            n2 = top neighbor of new_state 
            n3 = right-top neighbor of new_state 
            n4 = left neighbor of new_state 
            n5 = right neighbor of new_state 
            n6 = right-bottom neighbor of new_state
            n7 = bottom neighbor of new_state
            n8 = left-bottom neighbor of new_state
        -------------

        Returns:
            new_state = new state after applying the rule  
        """
        new_state = self.rm.apply(self.cells, self.neighbors)
        self.cells = new_state

        #Dont forget to update neighbors after evolution
        self.update_neighbors()
        return new_state

    def initialize_random_bin(self, ratio):
        """
        Initializes the ca randomly with a approximated ratio of 1 and 0 

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = (ratio > np.random.random(self.size)).astype(int) 
        self.update_neighbors()

    def initialize_random(self):
        """
        Initializes the CA randomly with random values from 0 to 1

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.random(self.size)
        self.update_neighbors()

    def initialize_zero(self):
        """
        Initializes the CA with zeros
        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.zeros(self.size)
        self.update_neighbors()
 
    def initialize_random_int(self, min_value, max_value):
        """
        Initializes the ca randomly with integers from min_value to max_value 

        Automatically updates neighbors after initialization
        -------------
        Parameters:
            min_value: lowest possible integer state
            max_value: highest possible integer state

        max_value - min_value = total number of state of the system
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.randint(min_value, max_value, size=self.size)  
        self.update_neighbors()
        
    def set_rule(self, rule_object):
        """
        Sets the default rule for animation of the object
        -------------
        Parameters:
            rule_object : An instance of a rule object that has an appropriate functions to update the cells for animation.
        -------------
        Returns
            None: Updates default rule
        """
        self.rm.set_rule(rule_object)

    def add_rule(self, rule_object):
        """
        Add the rule object to the rule manager.
        This rule will apply for every evolve() function call.
        """
        self.rm.add_rule(rule_object) 

    def reset_rule(self):
        """
        Resets the rule list from RuleManager
        """
        self.rm.reset_rule()
    
    #def run(self, iteration, collector=None):

    def animate(self, cmap='plasma', savefig=False):
        fig = plt.figure()
        self.im = plt.imshow(self.cells, cmap=cmap, animated=True)

        ani = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True)
        plt.show()

        if savefig:
            ani.save('Animation.mp4')

    def _update_fig(self, *args):
        self.im.set_array(self.evolve())
        return self.im,

class MooreCA_t(CA2D):
    def __init__(self, dim):
        CA2D.__init__(self, dim)
        self.neighborhood = "Toroidal Moore"
        print("You created a toroidal CA with Moore neighborhood")

    def update_neighbors(self):
        n2 = np.roll(self.cells, 1, axis=0)
        n1 = np.roll(n2, 1, axis=1)
        n3 = np.roll(n2, -1, axis=1)
        n4 = np.roll(self.cells, 1, axis=1)
        n5 = np.roll(self.cells, -1, axis=1)
        n7 = np.roll(self.cells, -1, axis=0)
        n6 = np.roll(n7, 1, axis=1)
        n8 = np.roll(n7, -1, axis=1)

        self.neighbors = {}
        self.neighbors['top-left'] = n1
        self.neighbors['top'] = n2
        self.neighbors['top-right'] = n3
        self.neighbors['left'] = n4
        self.neighbors['right'] = n5
        self.neighbors['bottom-left'] = n6
        self.neighbors['bottom'] = n7
        self.neighbors['bottom-right'] = n8


class VonCA_t(CA2D):
    def __init__(self, dim):
        CA2D.__init__(self, dim)
        self.neighborhood = "Toroidal Von Neumann"
        print("You created a toroidal CA with Von Neumann neighborhood")

    def update_neighbors(self):
        self.neighbors = {}
        self.neighbors['top'] = np.roll(self.cells, 1, axis=0)
        self.neighbors['left'] = np.roll(self.cells, 1, axis=1)
        self.neighbors['right'] = np.roll(self.cells, -1, axis=1)
        self.neighbors['bottom'] = np.roll(self.cells, -1, axis=0)

class MooreCA(CA2D):
    def __init__(self, dim):
        CA2D.__init__(self, dim)
        self.neighborhood = "Toroidal Moore"
        print("You created a NON-Toroidal CA with Moore neighborhood")

    def update_neighbors(self):
        n2 = np.roll(self.cells, 1, axis=0)
        n2[0,:] = 0
        n1 = np.roll(n2, 1, axis=1)
        n1[0,:] = 0
        n1[:,0] = 0
        n3 = np.roll(n2, -1, axis=1)
        n3[0,:] = 0
        n3[:,-1] = 0

        n4 = np.roll(self.cells, 1, axis=1)
        n4[:,0] = 0
        n5 = np.roll(self.cells, -1, axis=1)
        n5[:,-1] = 0

        n7 = np.roll(self.cells, -1, axis=0)
        n7[-1,:] = 0
        n7[:,0] = 0

        n6 = np.roll(n7, 1, axis=1)
        n6[-1,:] = 0

        n8 = np.roll(n7, -1, axis=1)
        n8[-1,:] = 0
        n8[:,-1] = 0

        self.neighbors = {}
        self.neighbors['top-left'] = n1
        self.neighbors['top'] = n2
        self.neighbors['top-right'] = n3
        self.neighbors['left'] = n4
        self.neighbors['right'] = n5
        self.neighbors['bottom-left'] = n6
        self.neighbors['bottom'] = n7
        self.neighbors['bottom-right'] = n8

class VonCA(CA2D):
    def __init__(self, dim):
        CA2D.__init__(self, dim)
        self.neighborhood = "Toroidal Von Neumann"
        print("You created a NON-Toroidal CA with Von Neumann neighborhood")

    def update_neighbors(self):
        n1 = np.roll(self.cells, 1, axis=0)
        n1[0,:] = 0
        n2 = np.roll(self.cells, 1, axis=1)
        n2[:,0] = 0
        n3 = np.roll(self.cells, -1, axis=1)
        n3[:,-1] = 0
        n4 = np.roll(self.cells, -1, axis=0)
        n4[-1,:] = 0

        self.neighbors = {}
        self.neighbors['top'] = n1
        self.neighbors['left'] = n2
        self.neighbors['right'] = n3
        self.neighbors['bottom'] = n4

class SimpleCA(CA2D):
    def __init__(self, dim):
        CA2D.__init__(self, dim)
        self.neighborhood = "Toroidal 2D-CA"
        self.neighbors = {}

    def update_neighbors(self):
        pass

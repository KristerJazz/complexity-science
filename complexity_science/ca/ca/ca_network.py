import numpy as np
import matplotlib.pyplot as plt
from .rule_manager import RuleManager
from .data_collector import DataCollector
#import matplotlib.animation as animation


class CA_Network:
    def __init__(self, adj_matrix, heterogeneity=1):
        """
        Creates an cellular automata object with a network neighborhood that is not lattice-trivial, given an initial adjacency network. See related initialize_ functions to initialize properly.
        ---------------
        Parameters:
            adj_matrix = adjacency matrix of the network
        ---------------
        Returns:
            None
        """
        self.adj = adj_matrix 
        self.size = len(self.adj)
        self.heterogeneity = heterogeneity
        self.cells = np.zeros([self.heterogeneity, self.size])
        self.rm = RuleManager()

    def evolve(self):
        """
        Evolves the CA according to the rule applied.
        Updates the state of the cell.
            cell = new_state

        -------------

        Returns:
            new_state = new state after applying the rule  
        """
        new_state = self.rm.apply(self.cells, self.adj)
        self.cells = new_state


    def initialize_population(self, N, p=None):
        self.cells[0,0] = 9000
        self.cells[1,0] = 1000
        self.cells[2,0] = 0
        self.cells[3,0] = 0
        #pop_sum = 0
        #while pop_sum != N:
        #    pop = np.random.random(self.size)
        #    pop = np.round(pop*100/pop.sum())
        #    pop_sum = pop.sum()

        #if not p:
        #    p = [1/self.heterogeneity]*self.heterogeneity

        #total = 0
        #for i in range(self.heterogeneity-1):
        #    fraction = np.round(p[i]*pop)
        #    self.cells[i] = fraction 
        #    total += fraction
        #self.cells[-1] = pop-total

    def initialize_random_bin(self, ratio):
        """
        Initializes the ca randomly with a approximated ratio of 1s and 0s 

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = (ratio > np.random.random(self.size)).astype(int) 

    def initialize_random(self):
        """
        Initializes the CA randomly with random values from 0 to 1

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.random(self.size)
    def initialize_zero(self):
        """
        Initializes the CA with zeros
        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.zeros(self.size)

    def initialize_index(self, tuple_index, value):
        """
        Initializes an index in the CA with a certain value and 0 for all the rest
        Automatically updates neighbors after initialization
        -------------
        Parameters:
            tuple_index : index on the matrix as tuple
            value : value of the initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.zeros(self.size)
        self.cells[index] = value
 
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
    def set_rule(self, rule_object):
        """
        Sets the default rule for animation of the object
        -------------
        Parameters:
            rule_object : An instance of a rule object that has an appropriate functions to update the cells for animation.
        -------------
        Returns
            None: Set default rule in rule manager 
        """
        self.rm.set_rule(rule_object)

    def add_rule(self, rule_object):
        """
        Add the rule object to the rule manager.
        This rule will apply for every evolve() function call.
        -------------
        Returns
            None: Add rule to rule manager
        """
        self.rm.add_rule(rule_object) 

    def reset_rule(self):
        """
        Removes all the rule from RuleManager
        -------------
        Returns
            None: Removes rules in rule manager
        """
        self.rm.reset_rule()

    def modify_rule(self, **kwargs):
        """
        Removes all the rule from RuleManager
        -------------
        Returns
            None: Modify parameters of rules in rule manager
        """
        self.rm.modify_rule(**kwargs)
    
    def run_collect(self, iteration, steady_state=False):#, collector = {'mean':np.average}):
        """
        Run evolution according to the number of iteration
        -------------
        Parameters:
            iteration = number of iteration
            collector = data reduction (sum, mean, max, min, std, etc)
       """
        T = iteration
        t = 0
        S = []
        I = []
        C = []
        R = []
        dt = []
        while t < T and not(self.cells[2,0] == 0 and self.cells[1,0] == 0):
            self.evolve()
            t = self.rm.rules[0].t
            S.append(self.cells[0,0])
            I.append(self.cells[1,0])
            C.append(self.cells[2,0])
            R.append(self.cells[3,0])
            dt.append(t)

        return [S,I,C,R,dt]

#    def animate(self, num_frames='all', cmap='plasma', savefig=False, writer=animation.writers['ffmpeg']):
#        """
#        Run animation
#        ------------
#        Parameters
#            Animation parameters
#        """
#        fig = plt.figure()
#        self.im = plt.imshow(self.cells, cmap=cmap, animated=True)
#
#        if num_frames=='all':
#            ani = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True)
#            plt.show()
#        else:
#            ani = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True, frames=num_frames, repeat=False)
#            plt.show()
#
#        if savefig:
#            ani.save('Animation.mp4', writer=writer)
#	
#    def jyp_anim(self, cmap='plasma'):
#        fig = plt.figure()
#        self.im = plt.imshow(self.cells, cmap=cmap, animated=True)
#        anim = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True)
#        return anim
#
#    def _update_fig(self, *args):
#        self.im.set_array(self.evolve())
#        return self.im,
#


class Gillespie(CA_Network):
    def __init__(self, adj, heterogeneity):
        CA_network.__init__(self, adj, heterogeneity)

    def evolve(self):
        prob = self.compute_prob(self.cells)
        new_state = self.rm.apply(self.cells, self.prob)
        self.cells = new_state

        return new_state

    def run_collect(self):
        pass

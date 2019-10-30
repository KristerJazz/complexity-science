import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .rules import RuleManager


class CA_3D:
    def __init__(self, dim):
        """
        Creates an 3D cellular automata object of a given dimension with random value from 0-1. See related initialize_ functions to initialize properly.
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
        self.update_neighbors()
        print("You initialized a 3D-CA with Moore neighborhood")

    def update_neighbors(self): 

        self.neighbors={}
        self.n2 = np.roll(self.cells, 1, axis=0)
        self.n2[0,:] = 0
        self.n1 = np.roll(self.n2, 1, axis=1)
        self.n1[0,:] = 0
        self.n1[:,0] = 0
        self.n3 = np.roll(self.n2, -1, axis=1)
        self.n3[0,:] = 0
        self.n3[:,-1] = 0

        self.n4 = np.roll(self.cells, 1, axis=1)
        self.n4[:,0] = 0
        self.n5 = np.roll(self.cells, -1, axis=1)
        self.n5[:,-1] = 0

        self.n7 = np.roll(self.cells, -1, axis=0)
        self.n7[-1,:] = 0
        self.n7[:,0] = 0

        self.n6 = np.roll(self.n7, 1, axis=1)
        self.n6[-1,:] = 0

        self.n8 = np.roll(self.n7, -1, axis=1)
        self.n8[-1,:] = 0
        self.n8[:,-1] = 0

        self.neighbors['top-left'] = self.n1
        self.neighbors['top'] = self.n2
        self.neighbors['top-right'] = self.n3
        self.neighbors['left'] = self.n4
        self.neighbors['right'] = self.n5
        self.neighbors['bottom-left'] = self.n6
        self.neighbors['bottom'] = self.n7
        self.neighbors['bottom-right'] = self.n8

        keys = list(self.neighbors)
        for i in [-1,1]:
            for key in keys:
                self.neighbors[key+str(i)] = np.roll(self.neighbors[key], shift=i, axis=2)

        self.neighbors['direct-left'] = np.roll(self.cells, shift =1, axis=2)
        self.neighbors['direct-right'] = np.roll(self.cells, shift =-1, axis=2)
        #print("The number of neighbors is, ", len(self.neighbors.keys()))
       
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
        self.cells = (np.random.random(self.size) > ratio).astype(int) 
        self.update_neighbors()

    def initialize_random(self):
        """
        Initializes the ca randomly with random values from 0 to 1

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.random(self.size)
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

    def try_3d_animate(self):
        self.rm.set_game_of_life()

        fig = plt.figure()
        pass 

        ani = animation.FuncAnimation(fig, self.update_fig, interval=50, blit=True)
        plt.show()

        self.rm.reset_rule()

        if savefig:
            ani.save('GameOfLife.mp4')

    def animate_game_of_life(self, cmap='plasma', savefig=False):
        self.rm.set_game_of_life()

        fig = plt.figure()
        self.im = plt.imshow(self.cell(), cmap=cmap ,animated=True)

        ani = animation.FuncAnimation(fig, self.update_fig, interval=50, blit=True)
        plt.show()

        self.rm.reset_rule()

        if savefig:
            ani.save('GameOfLife.mp4')

    def animate_brians_brain(self, cmap='plasma', savefig=False):
        self.rm.set_brians_brain()
        fig = plt.figure()
        self.im = plt.imshow(self.cell(), cmap=cmap, animated=True)

        ani = animation.FuncAnimation(fig, self.update_fig, interval=50, blit=True)
        plt.show()

        self.rm.reset_rule()

        if savefig:
            ani.save('BriansBrain.mp4')

    def update_fig(self, *args):
        self.cells = self.evolve()
        self.im.set_array(self.cell())
        return self.im,

    def cell(self):
        print(self.cells[:][:][0])
        return self.cells[:][:][0]



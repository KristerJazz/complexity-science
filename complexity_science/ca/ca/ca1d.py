import numpy as np
import matplotlib.pyplot as plt

from .rule_manager import RuleManager

class CA1D():
    def __init__(self, N):
        """
        Creates an uninitialized 1D cellular automata object with length N
        -------------
        Parameters:
            N = number of cells
            n1 : left neighbor
            n2 : right neighbor
        ------------- 
        Returns:
            None
        """
        self.num_cells = N
        self.cells = np.zeros([N])
        self.rm = RuleManager() 
        self.update_neighbors()

    def update_neighbors(self):
        """
        Updates the neighbor dictionary according to the neighborhood
        """
        raise NotImplementedError("This is the base 1D CA class; please use a CA with predetermined neighborhood; SimpleCA, CA_nt, CA_t.")

    def set_rule(self, rule_object):
        """
        Sets the CA rule to a wolfram rule number
        -------------
        Parameters:
            rule_number = values from (0-255). Refer to wolfram's rule numbers 
        -------------
        Returns:
            None
        """
        self.rm.set_rule(rule_object)

    def evolve(self):
        """
        Evolves the CA according to the rule applied.
        Updates the state of the cell.
            cell = new_state

        Updates the neighbor according to the new_state
            n1 = left neighbor of new_state
            n2 = right neighbor of new_state 
        -------------
        Returns:
            new_state = new state after applying the rule  
        """
        new_state = self.rm.apply(self.cells, self.neighbors)
        self.cells = new_state

        #Dont forget to update neighbors after evolution
        self.update_neighbors()

        return new_state

    def initialize_index(self, index_list):
        """
        Initializes the ca from the list of index
            cells[index] = 1

        Automatically updates neighbors after initialization
        -------------
        Parameters:
            index_list = list of index to be initialized with value 1 
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        assert(type(index_list)==type([])), "index_list must be a list"
        self.cells = np.zeros([self.num_cells], dtype=int)
        for i in index_list:
            self.cells[i] = 1

        self.update_neighbors()

    def initialize_binary(self, ratio):
        """
        Initializes the CA with a ratio of 1 and 0 values

        Automatically updates neighbors after initialization
        -------------
        Parameters:
            ratio = ratio of "1" state over the "0" state 
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = (np.random.random(self.num_cells)>ratio).astype(int) 
        self.update_neighbors()

    def reset(self):
        """
        Initializes the cells with zero values
        -------------
        Returns:
            None : Updates the cells to zero values
        """
        self.cells = np.zeros(self.num_cells)
        self.update_neighbors()

    def initialize_random(self):
        """
        Initializes the CA with a random value from 0 to 1 

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.random(self.num_cells) 
        self.update_neighbors()

    def run(self, iterations, show_figure=True):
        """
        Run cellular automata according to the wolfram rule_number assigned.
        -------------
        Parameters:
            iterations = number of times for the rule to be applied
            show_figure = Default is True, outputs the figure at run time
        -------------
        Returns:
            result = resulting N x iteration array of the CA evolution
        """
        result = [self.cells]
        for i in range(iterations):
            result.append(self.evolve())

        if show_figure:
            plt.imshow(result, cmap='Greens')
            plt.show()
        
        plt.clf()
        return result
        
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

class SimpleCA(CA1D):
    def __init__(self, N):
        CA1D.__init__(self, N)
        self.neighborhood = "No neighbors are automatically considered"

    def update_neighbors(self):
        """
        No neighors
        """
        pass

class CA_t(CA1D):
    def __init__(self, N):
        CA1D.__init__(self, N)
        self.neighborhood = "Two neighbors (left and right) are automatically considered"

    def update_neighbors(self):
        """
        Update the neighbor values
            n1 : left neighbor
            n2 : right neighbor
        -------------
        Returns:
            None
        """
        self.neighbors = {}
        self.neighbors['left'] = np.roll(self.cells, 1)
        self.neighbors['right'] = np.roll(self.cells, -1)

class CA_nt(CA1D):
    def __init__(self, N):
        CA1D.__init__(self, N)
        self.neighborhood = "Two neighbors (left and right) are automatically considered with non toroidal boundaries"

    def update_neighbors(self):
        """
        Update the neighbor values
            n1 : left neighbor
            n2 : right neighbor
        -------------
        Returns:
            None
        """
        self.neighbors = {}
        left = np.roll(self.cells, 1)
        left[0] = 0
        right = np.roll(self.cells, -1)
        right[-1] = 0
        self.neighbors['left'] = left 
        self.neighbors['right'] = right 

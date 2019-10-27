import numpy as np
import matplotlib.pyplot as plt

from .rules import RuleManager

class CA_1D():
    def __init__(self, N):
        """
        Creates an uninitialized 1D cellular automata object with length N
        -------------
        Parameters:
            N = number of cells
        ------------- 
        Returns:
            None
        """
        self.cells = np.zeros([N], dtype=int)
        self.rm = RuleManager() 
        self._initialize_neighbors()

    def _initialize_neighbors(self):
        """
        Initializes the neighbors with zero values 
        """
        self.n1 = np.roll(self.cells, 1)
        self.n2 = np.roll(self.cells, -1)

    def update_neighbors(self):
        """
        Update the neighbor values
            n1 : left neighbor
            n2 : right neighbor
        -------------
        Returns:
            None
        """
        self.n1 = np.roll(self.cells, 1)
        self.n2 = np.roll(self.cells, -1)

    def set_wolfram_rule(self, rule_number):
        """
        Sets the CA rule to a wolfram rule number
        -------------
        Parameters:
            rule_number = values from (0-255). Refer to wolfram's rule numbers 
        -------------
        Returns:
            None
        """
        self.rm.set_rule(rule_number)

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

        new_state = self.rm.apply(self.cells, self.n1, self.n2)
        self.cells = new_state

        #Dont forget to update neighbors after evolution
        self.update_neighbors()

        return new_state

    def initialize(self, index_list):
        """
        Initializes the ca from the list of index
            cells[index] = 1

        Automatically updates neighbors after initialization
            n1 : left neighbor
            n2 : right neighbor
        -------------
        Parameters:
            index_list = list of index to be initialized with value 1 
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        assert(type(index_list)==type([])), "index_list must be a list"
        for i in index_list:
            self.cells[i] = 1

        self.update_neighbors()

    def run_wolfram_rule(self, rule_number, iterations, show_figure=True):
        """
        Run cellular automata according to the wolfram rule_number assigned.
        -------------
        Parameters:
            rule_number = values from (0-255). Refer to wolfram's rule numbers
            iterations = number of times for the rule to be applied
            show_figure = Default is True, outputs the figure at run time
        -------------
        Returns:
            result = resulting N x iteration array of the CA evolution
        """
        self.set_wolfram_rule(rule_number)
        
        result = [self.cells]
        for i in range(iterations):
            result.append(self.evolve())

        if show_figure:
            plt.imshow(result, cmap='Greens')
            plt.show()

        return result
        
    def add_rule(self, rule_object):
        self.rm.add_rule(rule_object)

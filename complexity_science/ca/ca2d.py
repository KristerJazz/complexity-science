import numpy as np
from .rules import RuleManager


class CA_2D:
    def __init__(self, dim, dtype=int):
        """
        Creates an uninitialized 2D cellular automata object of a given dimension.
        ---------------
        Parameters:
            dim = cellular automata matrix shape
            dtype = data type (int, float ,double, etc)
        ---------------
        Returns:
            None
        """
        self.size = dim
        self.cells = np.random.random(dim)
        self.rm = RuleManager()
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
            n1 = top neighbor of new_state
            n2 = left neighbor of new_state 
            n3 = right neighbor of new_state
            n4 = bottom neighbor of new_state

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

class MOORE_CA_t(CA_2D):
    def __init__(self, dim, dtype=int):
        CA_2D.__init__(self, dim, dtype)
        self.neighborhood = "Toroidal Moore"
        print("You created a toroidal CA with Moore neighborhood")

    def update_neighbors(self):
        self.n2 = np.roll(self.cells, 1, axis=0)
        self.n1 = np.roll(self.n2, 1, axis=1)
        self.n3 = np.roll(self.n2, -1, axis=1)
        self.n4 = np.roll(self.cells, 1, axis=1)
        self.n5 = np.roll(self.cells, -1, axis=1)
        self.n7 = np.roll(self.cells, -1, axis=0)
        self.n6 = np.roll(self.n7, 1, axis=1)
        self.n8 = np.roll(self.cells, -1, axis=1)

class VON_CA_t(CA_2D):
    def __init__(self, dim, dtype=int):
        CA_2D.__init__(dim, dtype=dtype)
        self.neighborhood = "Toroidal Von Neumann"
        print("You created a toroidal CA with Von Neumann neighborhood")

    def update_neighbors(self):
        self.n1 = np.roll(self.cells, 1, axis=0)
        self.n2 = np.roll(self.cells, 1, axis=1)
        self.n3 = np.roll(self.cells, -1, axis=1)
        self.n4 = np.roll(self.cells, -1, axis=0)



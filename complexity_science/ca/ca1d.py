import numpy as np
from .rules import RuleManager

class CA_1D():
    def __init__(self, N):
        """
        Creates a 1D cellular automata object with length N
        -------------
        Parameters:
            N = number of cells
        
        Returns:
            None
        """
        self.cells = np.zeros([N], dtype=int)
        self.rm = RuleManager() 
        self._initialize_neighbors()

    def _initialize_neighbors(self):
        self.n1 = np.roll(self.cells, 1)
        self.n2 = np.roll(self.cells, -1)

    def update_neighbors(self):
        self.n1 = np.roll(self.cells, 1)
        self.n2 = np.roll(self.cells, -1)

    def evolve(self):
        new_state = self.rm.apply(self.cells, self.n1, self.n2) 

        #Dont forget to update neighbors after evolution
        self.cells = new_state
        self.update_neighbors()
        return new_state

    def set_rule(self, number):
        self.rm.set_rule(number)

    def initialize(self, index):
        self.cells[int(index)] = 1
        self.update_neighbors()

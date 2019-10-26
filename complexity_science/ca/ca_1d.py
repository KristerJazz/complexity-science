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
"""
class RuleManager:
    def __init__(self):
        self.rules = []
        self.wolfram_options = [Case7(), Case6(), Case5(), Case4(),
                                Case3(), Case2(), Case1(), Case0()]

    def set_rule(self, number):
        rule_in_binary = self._bin_convert(number)
        rule = np.array([int(x) for x in list(rule_in_binary)]) 
        
        for i, j in enumerate(rule):
            if j==1:
                self.rules.append(self.wolfram_options[i])
    
    def _bin_convert(self, rule_num):
        return format(rule_num, '08b')

    def apply(self, current, left, right):
        result = np.zeros(len(current), dtype=int)
        for rule in self.rules:
            result += rule.apply(current, left, right)
        return result

class Case0:
    def __init__(self):
        self.case_num = 0
    
    def apply(self, current, left, right):
        n1_state = (left==0)
        n2_state = (right==0)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==0).astype(int)
        return result

class Case1:
    def __init__(self):
        self.case_num = 1

    def apply(self, current, left ,right):
        n1_state = (left==0)
        n2_state = (right==1)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==0).astype(int)
        return result

class Case2:
    def __init__(self):
        self.case_num = 2

    def apply(self, current, left ,right):
        n1_state = (left==0)
        n2_state = (right==0)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==1).astype(int)
        return result

class Case3:
    def __init__(self):
        self.case_num = 3

    def apply(self, current, left ,right):
        n1_state = (left==0)
        n2_state = (right==1)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==1).astype(int)
        return result

class Case4:
    def __init__(self):
        self.case_num = 4

    def apply(self, current, left ,right):
        n1_state = (left==1)
        n2_state = (right==0)
        result = np.logical_and(n1_state, n2_state).astype(int)
        result = result*(current==0).astype(int)
        return result

class Case5:
    def __init__(self):
        self.case_num = 5

    def apply(self, current, left ,right):
        n1_state = (left==1)
        n2_state = (right==1)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==0).astype(int)
        return result

class Case6:
    def __init__(self):
        self.case_num = 6

    def apply(self, current, left ,right):
        n1_state = (left==1)
        n2_state = (right==0)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==1).astype(int)
        return result

class Case7:
    def __init__(self):
        self.case_num = 7

    def apply(self, current, left ,right):
        n1_state = (left==1)
        n2_state = (right==1)
        result = np.logical_and(n1_state, n2_state).astype(int)

        result = result*(current==1).astype(int)
        return result
"""

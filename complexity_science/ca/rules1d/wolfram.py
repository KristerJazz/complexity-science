import numpy as np

class Wolfram:
    def __init__(self, rule_number = None):
        self.rules = []
        self.set_rule(rule_number)

    def set_rule(self, number):
        wolfram_options = [Bit128(), Bit64(), Bit32(), Bit16(),
                           Bit8(), Bit4(), Bit2(), Bit1()]

        rule_in_binary = self._bin_convert(number)

        rule = np.array([int(x) for x in list(rule_in_binary)]) 
        
        for i, j in enumerate(rule):
            if j==1:
                self.rules.append(wolfram_options[i])

    def _bin_convert(self, rule_num):
        return format(rule_num, '08b')

    def apply(self, current, neighbors_dict):
        result = np.zeros_like(current)
        for rule in self.rules:
            result += rule.apply(current, neighbors_dict) 
        return result

class Bit1:
    def __init__(self):
        self.case_num = 0
    
    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==0)
        n2_state = (right==0)
        current_state = (current==0)
    
        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit2:
    def __init__(self):
        self.case_num = 1
        
    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==0)
        n2_state = (right==1)
        current_state = (current==0)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit4:
    def __init__(self):
        self.case_num = 2

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==0)
        n2_state = (right==0)
        current_state = (current==1)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit8:
    def __init__(self):
        self.case_num = 3

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==0)
        n2_state = (right==1)
        current_state = (current==1)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit16:
    def __init__(self):
        self.case_num = 4

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==1)
        n2_state = (right==0)
        current_state = (current==0)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit32:
    def __init__(self):
        self.case_num = 5

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==1)
        n2_state = (right==1)
        current_state = (current==0)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit64:
    def __init__(self):
        self.case_num = 6

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==1)
        n2_state = (right==0)
        current_state = (current==1)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

class Bit128:
    def __init__(self):
        self.case_num = 7

    def apply(self, current, neighbors):
        left = neighbors['left']
        right = neighbors['right']

        n1_state = (left==1)
        n2_state = (right==1)
        current_state = (current==1)

        result = np.logical_and(n1_state, n2_state)
        result = np.logical_and(result, current_state).astype(int)
        return result

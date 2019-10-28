import numpy as np

class RuleManager:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule_object):
        self.rules.append(rule_object)

    def reset_rule(self):
        self.rules = []

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

class GameOfLife:
    def apply(self, current, neighbors):
        for key in neighbors:
            total_neighbors += neighbors[keys]

        result = np.zeros_like(current)
        state = current.copy()

        live = (current==1)
        dead = (current==0)
        two = (total_neighbors == 2)
        three = (total_neighbors ==3)

        less_two = (total_neighbors < 2)
        more_three = (total_neighbors >3)
        two_or_three = np.logical_or(two,three)

        result += np.logical_and(live, two_or_three).astype(int)
        result += np.logical_and(dead, three).astype(int)

        state -= np.logical_and(live, less_two).astype(int)
        state -= np.logical_and(live, more_three).astype(int)

        result += state

        return result
"""
class RuleManager1D(RuleManager):
    def __init__(self):
        RuleManager.__init__()

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

    def apply(self, current, left, right):
        result = np.zeros(len(current), dtype=int)
        for rule in self.rules:
            result += rule.apply(current, left, right)
        return result


class RuleManager2D(RuleManager):
    def __init__(self):
        RuleManager.__init__()

    def apply(self, current, left, right):
        result = np.zeros(len(current), dtype=int)
        for rule in self.rules:
            result += rule.apply(current, left, right)
        return result
"""



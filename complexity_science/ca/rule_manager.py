import numpy as np
from .rules1d.wolfram import Wolfram 

class RuleManager:
    def __init__(self):
        self.rules = []
        self.default = 0

    def add_rule(self, rule_object):
        self.rules.append(rule_object)

    #def set_default(self, rule_object):
    #    self.default = rule_object

    #def add_default(self):
    #    if self.default:
    #        self.add_rule(self.default)

    #def reset_rule(self):
    #    self.rules = []

    def set_rule(self, rule_object):
        self.rules.append(rule_object)
        
    #def _bin_convert(self, rule_num):
    #    return format(rule_num, '08b')

    def apply(self, current, neighbors_dict):
        result = current.copy() 
        for rule in self.rules:
            new_state = rule.apply(result, neighbors_dict) 
            result = new_state

        return new_state 


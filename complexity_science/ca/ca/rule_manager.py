import numpy as np

class RuleManager:
    def __init__(self):
        self.rules = []
        self.default = 0

    def add_rule(self, rule_object):
        self.rules.append(rule_object)

    def reset_rule(self):
        self.rules = []

    def set_rule(self, rule_object):
        self.rules.append(rule_object)
        
    def apply(self, current, neighbors_dict):
        result = current.copy() 
        for rule in self.rules:
            new_state = rule.apply(result, neighbors_dict) 
            result = new_state

        return new_state 


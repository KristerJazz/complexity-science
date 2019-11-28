from .ca.ca1d import *
from .rules1d.wolfram import Wolfram 

def wolfram(N, rule_numbers, toroidal=True):
    if toroidal:
        model = CA_t(N)
    else:
        model = CA_nt(N)

    if (type(rule_numbers) == type(int())):
        model.set_rule(Wolfram(rule_numbers))

    elif (type(rule_numbers) == type([])):
        for num in rule_numbers:
            model.add_rule(Wolfram(num))
    else:
        print("Please input a valid rule number or a list of rule number")

    return model

from .ca.ca2d import *
from .rules2d.brians import *
from .rules2d.game_of_life import *
from .rules2d.applause import *

def brians_brain(dim, toroidal=True, default=True):
    if toroidal:
        model = MooreCA_t(dim)
    else:
        model = MooreCA(dim)

    if default:
        model.set_rule(BriansBrain())

    model.initialize_random_int(0,3)
    return model

def game(dim, toroidal=True, default=True):
    if toroidal:
        model = MooreCA_t(dim)
    else:
        model = MooreCA(dim)

    if default:
        model.set_rule(GameOfLife())

    model.initialize_random_bin(0.5)
    return model

def applause(dim, rule_object='default', simple=True):
    if simple:
        model = MooreCA_t(dim)

    if (rule_object=='default'):
        params = {}
        params['a'] = 0.5
        params['b'] = 0.3
        params['alpha'] = 1
        params['beta'] = 5

        print('Applause rule is set')
        model.set_rule(Applause(params))
    else:
        model.set_rule(rule_object)

    model.initialize_random_bin(0.9)
        print(self.cells)

    return model

def mpa(dim, toroidal=True, params=None):
    if toroidal:
        model = VonCA_t(dim)
    else:
        model = VonCA(dim)

    #if params:
    #    model.
    model.initialize_random()
    return model



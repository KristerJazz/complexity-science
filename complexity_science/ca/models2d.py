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

def mpa(dim, toroidal=True, params=None):
    if toroidal:
        model = VonCA_t(dim)
    else:
        model = VonCA(dim)

    #if params:
    #    model.
    return model

    model.initialize_random()

def applause(dim, rule_object='default', simple=True):
    if simple:
        model = SimpleCA(dim)

    if 'default':
        #model.set_rule()
        pass

    model.initialize_random_bin(1)
    return model

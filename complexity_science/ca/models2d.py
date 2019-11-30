from .ca.ca2d import *
from .rules2d.brians import *
from .rules2d.game_of_life import *
from .rules2d.applause import *
from .rules2d.mpa import *

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


def applause(dim, rule_object='default', simple=True, **kwargs):
    if simple:
        model = MooreCA_t(dim)

    if (rule_object=='default'):
        model.set_rule(Applause(**kwargs))
    else:
        model.set_rule(rule_object)

    model.initialize_random_bin(0.9)
    return model


def mpa(dim, rule_object='default', toroidal=True, **kwargs):
    if toroidal:
        model = VonCA_t(dim)
    else:
        model = VonCA(dim)

    if rule_object=='default':
        dt = 0.001
        D = 30
        beta = 0.8
        #growth params
        params = {}
        params['dt'] = dt
        params['beta'] = beta
        params['D'] = D
        params['alpha'] = D*dt

    else:
        model.set_rule(rule_object)

    model.initialize_random()
    return model

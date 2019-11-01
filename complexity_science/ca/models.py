from .ca2d import *
from .rules import *

def brians_brain(dim, toroidal=True, default=True):
    if toroidal:
        model = MOORE_CA_t(dim)
    else:
        model = MOORE_CA(dim)

    if default:
        model.set_default(BriansBrain())

    model.initialize_random_int(0,3)
    return model

def game_of_life(dim, toroidal=True, default=True):
    if toroidal:
        model = MOORE_CA_t(dim)
    else:
        model = MOORE_CA(dim)

    if default:
        model.set_default(GameOfLife())

    model.initialize_random_bin(0.5)
    return model

def mpa(dim, toroidal=True):
    if toroidal:
        model = VON_CA_t(dim)
    else:
        model = VON_CA(dim)

    return model

    model.initialize_random()

def applause(dim, simple=True):
    if simple:
        model = Simple_CA(dim)

    model.initialize_random_bin(1)
    return model

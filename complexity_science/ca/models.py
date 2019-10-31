from .ca2d import *
from .rules import *

def briansbrain(dim, toroidal=True, default=True):
    if toroidal:
        model = MOORE_CA_t(dim)
    else:
        model = MOORE_CA(dim)

    if default:
        model.set_default(BriansBrain())

    return model


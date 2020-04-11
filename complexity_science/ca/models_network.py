import numpy as np
from .ca.ca_network import *
from .rules_network.migration import *
from .rules_network.gillespie import *

def gillespie(adj, heterogeneity=4, rule='default'):
    model = CA_Network(adj, heterogeneity)
    if rule=='default':
        model.set_rule(SIRC_Gillespie())
        #model.add_rule(Migration())
    return model

def migration(adj):
    model = CA_Network(adj,3)
    model.set_rule(Migration())
    return model

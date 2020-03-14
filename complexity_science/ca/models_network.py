import numpy as np
from .ca.ca_network import *
from .rules_network.migration import *
from .rules_network.gillespie import *

def guillespie(adj, heterogeneity=4, rule='default'):
    model = CA_Network(adj, heterogeneity)
    if rule=='default':
        model.add_rule(SIRC_Gillespie())
        print("Added model")
    return model

def migration(adj):
    model = CA_Network(adj,3)
    model.add_rule(Migration())
    return model

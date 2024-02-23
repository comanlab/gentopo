import networkx as nx
import numpy as np
from gentopo.topology.families import families


class SmallWorldReference(object):
    """Generate and constrain a list of small world networks.

    Attributes:
        object (_type_): _description_
    """

    def __init__(self, nlist: list, kmin: int, kmean: int, kmax: int) -> None:
        """Initializes the small world reference topologies (random and lattice) with k-neighbor constraints

        Args:
            nlist (list):
            kmin (int): minimum neighbors
            kmean (int): mean neighbors
            kmax (int): maximum neighbors
        """
        self.nlist = nlist
        self.kmin = kmin
        self.kmax = kmax
        self.kmean = kmean
        self.random_topology = {}
        self.lattice_topology = {}

    def generate(self):
        for n in self.nlist:
            self.lattice_topology[n] = families.lattice(n, self.kmean)
            self.random_topology[n] = nx.random_reference(self.lattice_topology[n], n)


def omega(G, Lr, Cl):
    # TODO where G is the generated to compare to metrics from random and lattice metrics

    C = nx.average_clustering(G)
    L = nx.average_shortest_path_length(G)

    return (Lr / L) - (C / Cl)


def random_reference():
    pass

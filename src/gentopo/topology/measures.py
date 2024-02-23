import networkx as nx
import numpy as np
from gentopo.topology.families import families


class SmallWorldReference(object):
    """Generate and constrain a list of small world networks."""

    def __init__(self, nlist: list, kmin: int, kmean: int, kmax: int) -> None:
        """Initializes the small world reference topologies (random and lattice) with
        k-neighbor constraints

        Args:
            nlist: List of network sizes
            kmin: Minimum neighbors any node can have
            kmean: Mean neighbors that are desired
            kmax: Maximum neighbors any node can have

        Attributes:
            nlist: List of network sizes
            kmin: Minimum neighbors any node can have
            kmean: Mean neighbors that are desired
            kmax: Maximum neighbors any node can have
            random_topology:
        """
        self.nlist = nlist
        self.kmin = kmin
        self.kmax = kmax
        self.kmean = kmean
        self.random_topology: dict[str, nx.Graph] = {}
        self.lattice_topology: dict[str, nx.Graph] = {}

    def generate(self):
        for n in self.nlist:
            self.lattice_topology[n] = families.lattice(n, self.kmean)
            self.random_topology[n] = nx.random_reference(self.lattice_topology[n], n)


def omega(G: nx.Graph, Lr: float, Cl: float) -> float:
    # TODO where G is the generated to compare to metrics from random and lattice metrics

    C = nx.average_clustering(G)
    L = nx.average_shortest_path_length(G)

    return (Lr / L) - (C / Cl)


def random_reference():
    pass

import networkx as nx
import random
from gentopo.utils.decorators import Registry


# A registry for network families that can be generated with GenTopo
families = Registry()


@families.register
def lattice(n: int, k: int) -> nx.Graph:
    if k == n:
        return nx.complete_graph(n)

    G = nx.Graph()
    nodes = list(range(n))

    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]
        G.add_edges_from(zip(nodes, targets))

    return G


#
@families.register
def small_world(n: int, k: int, p: float, rounds: int) -> nx.Graph:
    """
    Generates a connected small world network with n nodes.
    """
    if k == n:
        return nx.complete_graph(n)

    # Start with a ring lattice with k-neighbors per node
    G = families.lattice(n, k)
    nodes = list(G.nodes)

    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]
        for u, v in zip(nodes, targets):
            # skip if u has as many edges as possible rounds
            if G.degree(u) >= rounds:
                continue
            if random.random() < p:
                w = random.choice(nodes)
                # enforce no self loops or multiple edges
                while w == u or G.has_edge(u, w):
                    w = random.choice(nodes)
                # skip if w has as many edges as possible rounds
                if G.degree(w) >= rounds:
                    continue
                G.remove_edge(u, v)
                G.add_edge(u, w)
    return G


@families.register
def connected_small_world(n: int, k: int, p: float, rounds: int, tries: int = 100):
    for i in range(tries):
        G = families.small_world(n, k, p, rounds)
        if nx.is_connected(G):
            break
        raise nx.NetworkXError("Maximum number of tries exceeded")
    return G


"""
    sufficient = False
    while not sufficient:
        graph = nx.connected_watts_strogatz_graph(n, k, p, tries=100)
        omega = nx.smallworld.omega(graph)
        print(f"Value of omega: {omega}")

        if min(omega_range) <= omega <= max(omega_range):
            print(f"Ideal topology found with omega between {omega_range}")
            sufficient = True

    return graph
"""

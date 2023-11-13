import networkx as nx
import matplotlib.pyplot as plt


def small_world(n_participants, k_ties, p):
    graph = nx.newman_watts_strogatz_graph(n=n_participants, k=k_ties, p=p)

    positions = nx.circular_layout(graph)

    plt.figure(figsize=(10, 10))
    topology_visual = nx.draw_networkx(graph, positions)

    # TODO: return a dict of metadata like inputs/drawing with topologiy data
    return graph

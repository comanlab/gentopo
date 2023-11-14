import networkx as nx
import matplotlib.pyplot as plt


def small_world(params):
    """
    Generates a small world network with n nodes.
    """
    try:
        n, k, p = params.values()
    except KeyError:
        raise ValueError("Invalid params for newman_watts_strogatz_graph.")

    graph = nx.newman_watts_strogatz_graph(n, k, p)

    positions = nx.circular_layout(graph)

    plt.figure(figsize=(10, 10))
    topology_visual = nx.draw_networkx(graph, positions)

    # TODO: return a dict of metadata like inputs/drawing with topologiy data
    return graph

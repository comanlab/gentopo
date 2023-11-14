import networkx as nx
import matplotlib.pyplot as plt


def positions(graph):
    return nx.circular_layout(graph)


def visualize(graph, path=None):
    """
    Draws a circular layout of the graph and defaults to not saving to file.
    """
    plt.figure(figsize=(10, 10))
    topology_visual = nx.draw_networkx(graph, positions(graph))

    if path:
        plt.savefig(path)

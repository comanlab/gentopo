import networkx as nx
import matplotlib.pyplot as plt


def complete(n):
    graph = nx.complete_graph(n)

    positions = nx.circular_layout(graph)

    plt.figure(figsize=(10, 10))
    topology_visual = nx.draw_networkx(graph, positions)

    # TODO: return a dict of metadata like inputs/drawing with topologiy data
    return graph

import os
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


def is_topology_dir(p, d):
    return os.path.isdir(os.path.join(p, d)) and re.search("topology", d) is not None


def create_topology_dir(study_name):
    topology_dirs = [d for d in os.listdir(dir_path) if is_topology_dir(dir_path, d)]
    topology_id = max([int(id.split("_")[1]) for id in topology_dirs]) + 1
    os.mkdir(f"studies/{study_name}/{topology_id}")
    return topology_id

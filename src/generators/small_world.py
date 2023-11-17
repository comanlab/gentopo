import networkx as nx


def small_world(params, seed=None):
    """
    Generates a small world network with n nodes.
    """
    try:
        n, k, p = params.values()
    except KeyError:
        raise ValueError("Invalid params for connected_watts_strogatz_graph.")

    return nx.connected_watts_strogatz_graph(n, k, p, tries=100, seed=seed)

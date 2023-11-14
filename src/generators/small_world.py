import networkx as nx


def small_world(params, seed=None):
    """
    Generates a small world network with n nodes.
    """
    try:
        n, k, p = params.values()
    except KeyError:
        raise ValueError("Invalid params for watts_strogatz_graph.")

    return nx.watts_strogatz_graph(n, k, p, seed)

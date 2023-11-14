import networkx as nx


def small_world(params):
    """
    Generates a small world network with n nodes.
    """
    try:
        n, k, p = params.values()
    except KeyError:
        raise ValueError("Invalid params for newman_watts_strogatz_graph.")

    return nx.newman_watts_strogatz_graph(n, k, p)

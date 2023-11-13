import networkx as nx
import matplotlib.pyplot as plt

graph = nx.newman_watts_strogatz_graph(
    n=NUMBER_OF_PARTICIPANTS, k=NUMBER_OF_TIES, p=PROBABILITY_OF_NEW_EDGE
)

positions = nx.circular_layout(graph)

plt.figure(figsize=(10, 10))
topology_visual = nx.draw_networkx(graph, positions)

import matplotlib.pyplot as plt
import networkx as nx
from utils import load

# load the graph
which = 2
adjacencies, fields, people = load()
G = nx.from_numpy_matrix(adjacencies[:, :, which])
labels = dict(zip(range(len(people)), people))
nx.set_node_attributes(G, name='name', values=labels)
remove = [k for k, v in G.degree() if v < 2]
G.remove_nodes_from(remove)
#G = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]

# draw graph
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)
labels = dict((n, d['name']) for n,d in G.nodes(data=True))
nx.draw_networkx_labels(G, pos, labels=labels)

plt.title(fields[which])
plt.axis('off')
plt.show()

import collections

import matplotlib.pyplot as plt
import networkx as nx

from utils import load

# load the graph
which = 0
adjacencies, fields, people = load()
G = nx.from_numpy_matrix(adjacencies[:, :, which], create_using=nx.DiGraph())


# In degree
in_degree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)
print("In degree sequence", in_degree_sequence)
in_degreeCount = collections.Counter(in_degree_sequence)
in_deg, in_cnt = zip(*in_degreeCount.items())

# Out degree
out_degree_sequence = sorted([d for n, d in G.out_degree()], reverse=True)
print("Out degree sequence", out_degree_sequence)
out_degreeCount = collections.Counter(out_degree_sequence)
out_deg, out_cnt = zip(*out_degreeCount.items())

# Degree
G = G.to_undirected()
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
print("Degree sequence", degree_sequence)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())


# Histogram
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')
plt.plot(in_deg, in_cnt, 'ro-')  # in-degree
plt.plot(out_deg, out_cnt, 'bv-') # out-degree

plt.title("Degree Histogram")
plt.ylabel("Number of nodes")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)

plt.show()

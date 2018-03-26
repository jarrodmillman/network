import sys

import matplotlib.pyplot as plt
import networkx as nx
from utils import load, node_options, edge_options

# load the graph
adjacencies, fields, people = load()
graphs = ['collaborate', 'communicate', 'familiar', 'dontknow']

for field, graph in enumerate(graphs):
    G = nx.from_numpy_matrix(adjacencies[:, :, field])

    # draw graph
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, **node_options)
    nx.draw_networkx_edges(G, pos, **edge_options)
    plt.axes().set_aspect('equal')
    plt.axis('off')
    plt.savefig(f'../slides/figs/{graph}.png')
    plt.clf()
    plt.close()

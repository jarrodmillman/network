import networkx as nx

from utils import load

adjacencies, fields, people = load()

for which, field in enumerate(fields):
    # create nx graph
    G = nx.from_numpy_matrix(adjacencies[:, :, which])
    G.name = field

    # print centrality information
    print()
    print(field)
    print('-' * len(field))
 
    print("Betweenness")
    b = nx.betweenness_centrality(G)
    for v in G.nodes():
        print("%0.2d %5.3f" % (v, b[v]))
    
    print("Degree centrality")
    d = nx.degree_centrality(G)
    for v in G.nodes():
        print("%0.2d %5.3f" % (v, d[v]))
    
    print("Closeness centrality")
    c = nx.closeness_centrality(G)
    for v in G.nodes():
        print("%0.2d %5.3f" % (v, c[v]))


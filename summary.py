import networkx as nx

from utils import load

adjacencies, fields, people = load()

for which, field in enumerate(fields):
    # create nx graph
    G = nx.from_numpy_matrix(adjacencies[:, :, which])
    G.name = field

    # print summary information
    print('-' * 50)
    print(nx.info(G))
    print()

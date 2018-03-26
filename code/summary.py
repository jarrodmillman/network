import networkx as nx

from utils import load

adjacencies, fields, people = load()

for f, field in enumerate(fields):
    # create nx graph
    G = nx.from_numpy_matrix(adjacencies[:, :, f])
    G.name = field

    # print summary information
    print('-' * 50)
    print(nx.info(G))
    print(f'Density: {nx.density(G)}')
    print()

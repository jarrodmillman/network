import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from utils import load

# load the graph
which = 1
adjacencies, fields, people = load()
G = nx.from_numpy_matrix(adjacencies[:, :, which])


L = nx.normalized_laplacian_matrix(G)
e = np.linalg.eigvals(L.A)
print("Largest eigenvalue:", max(e))
print("Smallest eigenvalue:", min(e))
plt.hist(e, bins=100)  # histogram with 100 bins
plt.xlim(0, 2)  # eigenvalues between 0 and 2
plt.title(fields[which])
plt.show()

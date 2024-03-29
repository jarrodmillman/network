import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from utils import node_options, edge_options

n_samples = 60
n_features = 26
mean = np.zeros(n_features)

true_corr = pd.read_csv('../data/correlation.csv', index_col=0)
gram = true_corr.dot(true_corr.T)

prng = np.random.RandomState(1)
X = prng.multivariate_normal(mean, gram, size=n_samples)
corr = np.corrcoef(X.T)

fig = plt.figure()
gs = gridspec.GridSpec(2, 3)

ax = fig.add_subplot(gs[0, :])
ax.plot(X)
plt.title('Timeseries data')
plt.axis('off')

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
ax = fig.add_subplot(gs[1, 0])
sns.heatmap(corr, ax=ax, cmap=cmap, cbar=False, square=True, linewidths=.5)
plt.title('Correlation matrix')
plt.axis('off')

ax = fig.add_subplot(gs[1, 1])
thres = np.abs(corr) > 0.6
sns.heatmap(thres, cbar=False, square=True, linewidths=.5, ax=ax)
plt.title('Threshold ($\pm 0.6$)')
plt.axis('off')


ax = fig.add_subplot(gs[1, 2], aspect='equal')
G = nx.from_numpy_matrix(thres)
pos = nx.circular_layout(G)
small_node_options = node_options.copy()
small_node_options['node_size'] = 20
nx.draw_networkx_nodes(G, pos, ax=ax, **small_node_options)
nx.draw_networkx_edges(G, pos, ax=ax, **edge_options)
plt.axis('off')
plt.title('Inferred graph')
plt.savefig('../slides/figs/infer_edges.png')

plt.clf()
plt.close()
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, **node_options)
nx.draw_networkx_edges(G, pos, **edge_options)
plt.axes().set_aspect('equal')
plt.axis('off')
plt.savefig('../slides/figs/inferred_graph.png')


plt.clf()
plt.close()
plt.hist(np.ravel(corr), bins=30)
plt.savefig('../slides/figs/hist.png')

plt.clf()
plt.close()
G = nx.from_numpy_matrix(true_corr.as_matrix())
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, **node_options)
nx.draw_networkx_edges(G, pos, **edge_options)
plt.axes().set_aspect('equal')
plt.axis('off')
plt.savefig('../slides/figs/true_graph.png')

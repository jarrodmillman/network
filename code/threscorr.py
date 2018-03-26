import numpy as np
from scipy import linalg
import pandas as pd
import networkx as nx

n_samples = 60
n_features = 26
mean = np.zeros(n_features)
#cov = pd.read_csv('covariance.csv', index_col=0)

true_corr = pd.read_csv('../data/correlation.csv', index_col=0)
gram = true_corr.dot(true_corr.T)

prng = np.random.RandomState(1)
X = prng.multivariate_normal(mean, gram, size=n_samples)

#plt.plot(X, legend=None)

corr = np.corrcoef(X.T)

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

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
sns.heatmap(corr, ax=ax, cmap=cmap, cbar=False,
            square=True, linewidths=.5)
plt.title('Correlation matrix')
plt.axis('off')

ax = fig.add_subplot(gs[1, 1])
thres = np.abs(corr) > 0.6
sns.heatmap(thres, cbar=False, square=True, linewidths=.5, ax=ax)
plt.title('Threshold ($\pm 0.6$)')
plt.axis('off')


ax = fig.add_subplot(gs[1, 2], aspect='equal')
#plt.sca(ax)
G = nx.from_numpy_matrix(thres)
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=20, node_color='royalblue', edgecolors='white', ax=ax)
nx.draw_networkx_edges(G, pos, alpha=0.7, ax=ax)
#labels = dict((n, d['name']) for n,d in G.nodes(data=True))
#nx.draw_networkx_labels(G, pos, labels=labels)
plt.axis('off')
plt.title('Inferred graph')
plt.savefig('../slides/figs/infer_edge1.png')

plt.clf()
plt.close()
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=20, node_color='royalblue', edgecolors='white')
nx.draw_networkx_edges(G, pos, alpha=0.7)
plt.axes().set_aspect('equal')
plt.axis('off')
plt.savefig('../slides/figs/inferred_graph.png')


plt.clf()
plt.close()
plt.hist(corr)
plt.savefig('../slides/figs/hi.png')

plt.clf()
plt.close()
G = nx.from_numpy_matrix(true_corr.as_matrix())
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=20, node_color='royalblue', edgecolors='white')
nx.draw_networkx_edges(G, pos, alpha=0.7)
plt.axes().set_aspect('equal')
plt.axis('off')
plt.savefig('../slides/figs/true_graph.png')

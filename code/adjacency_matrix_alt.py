import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from utils import load

# load the graph
adjacencies, fields, people = load()
N = len(people)

import matplotlib.pyplot as plt

fields = np.delete(fields, 3)
adjacencies = np.delete(adjacencies, 3, 2)
f, axes = plt.subplots(2, 3)
axes = axes.ravel()

for f, field in enumerate(fields):
    sns.heatmap(adjacencies[..., f], cbar=False, square=True, linewidths=.5, ax=axes[f])
    axes[f].set_title(field, fontsize="medium", fontweight="bold")
    axes[f].axis('off')


plt.savefig('../slides/figs/adjacency1.png')

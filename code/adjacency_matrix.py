import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from utils import load

# load the graph
adjacencies, fields, people = load()
N = len(people)

import matplotlib.pyplot as plt

f, axes = plt.subplots(2, math.ceil(len(fields) / 2))
axes = axes.ravel()

for f, field in enumerate(fields):
    axes[f].imshow(adjacencies[..., f], cmap='gray', vmin=0, vmax=1)
    axes[f].set_title(field)
    axes[f].set_xticks(np.arange(N))
    axes[f].set_xticklabels(people,
                            rotation=45, horizontalalignment='right')
    axes[f].set_xlabel('Participant')
    axes[f].set_yticks(np.arange(N))
    axes[f].set_yticklabels(people, rotation=45,
                            horizontalalignment='right')
    axes[f].set_ylabel('Response by')

if len(fields) < len(axes):
    axes[-1].axis('off')

if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/adjacency.png')
else:
    plt.show()
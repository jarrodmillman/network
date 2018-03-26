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
f, axes = plt.subplots(2, 3)#math.ceil(len(fields) / 2),
                       #figsize=(12, 6))#, sharey=True,
                       #sharex=True)
axes = axes.ravel()

for f, field in enumerate(fields):
    sns.heatmap(adjacencies[..., f], cbar=False, square=True, linewidths=.5, ax=axes[f])
    #axes[f].imshow(adjacencies[..., f], cmap='gray', vmin=0, vmax=1)
    axes[f].set_title(field)#, fontsize="small", fontweight="bold")
#    axes[f].set_xlabel('Participant', fontsize="small")
#    axes[f].set_ylabel('Response by', fontsize="small")
    axes[f].axis('off')


#if len(fields) < len(axes):
#    axes[-1].axis('off')

if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/adjacency1.png')
else:
    plt.show()

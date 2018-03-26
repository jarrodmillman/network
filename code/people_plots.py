import sys
from collections import OrderedDict

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../data/questionaire.csv')

# What best describes you?
question = 'What best describes you?'
df[question][17] = 'Other'  # I am a frankenstein of appointments.

fig, axes = plt.subplots(figsize=(12, 6), nrows=2, tight_layout=True,
    gridspec_kw={"hspace": 0.4})
ax = axes[0]

data = df[question].value_counts()
ax.bar(np.arange(len(data)), data, color="0")
xlabels = data.index
x_data, y_data = np.arange(len(data)), data

ax.bar(x_data, y_data, align='center', color="0")
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(
    xlabels,
    fontweight="bold")
ax.set_ylim(0, max(y_data) + 2)

ax.set_yticks([])
for x, y in zip(x_data, y_data):
    ax.text(x, y-0.95, '%d' % y, ha='center', va= 'bottom', fontweight="bold",
            color="1")

# hacky way of putting less tick labels
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.spines["left"].set_linewidth(0)
ax.set_title("Jarrod, please fix me", fontweight="bold")

ax = axes[1]
# I do work in (check all that apply):
question = 'I do work in (check all that apply):'
fields = ('Humanities',
          'Social sciences',
          'Natural sciences',
          'Computer science',
          'Software development',
          'Information technology',
          'Mathematics',
          'Statistics')

D = OrderedDict([(field, 0) for field in fields])
for response in df[question]:
    for field in fields:
        if field in response:
            D[field] += 1

#plt.rc('text', usetex=True)
x_data, y_data = np.arange(len(D)), list(D.values())
ax.bar(x_data, y_data, align='center', color="0")
xlabels = [k.replace(' ', '\n') for k in D.keys()]
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(
    xlabels, #fontsize="small",
    fontweight="bold")

ax.set_yticks([])
for x, y in zip(x_data, y_data):
    ax.text(x, y-1.15, '%d' % y, ha='center', va= 'bottom', fontweight="bold",
            color="1")

# hacky way of putting less tick labels
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.spines["left"].set_linewidth(0)
ax.set_ylim(0, max(y_data) + 2)

if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/work_in.png')
    plt.close()
else:
    plt.title("I do work in…", fontweight="bold")
    plt.show()


# How often do you?
# will also want to add node information to graphs...
activities = {'Collect data': 'How often do you: [Collect data]',
              'Analyze data': 'How often do you: [Analyze data]',
              'Design methods \n and algorithms': 'How often do you: [Design methods and algorithms]',
              'Implement algorithms': 'How often do you: [Implement algorithms]',
              'Write scripts': 'How often do you: [Write scripts]',
              'Write software \n packages': 'How often do you: [Write software packages]'}
freq = ['Never', 'Seldom', 'Sometime', 'Often']
how_often = pd.DataFrame(columns=freq, index=activities)

for k, v in activities.items():
    s = df[v]
    how_often.loc[k] = pd.Series({
        'Never': sum(s == 'Never'),
        'Seldom': sum(s == 'Seldom'),
        'Sometime': sum(s == 'Sometime'),
        'Often': sum(s == 'Often')})

how_often.plot.barh(rot=0, figsize=(12, 8)) #, fontsize="small")
#plt.gca().invert_yaxis()
if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/how_often.png')
    plt.close()
else:
    plt.title('How often do you?')
    plt.show()

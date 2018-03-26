import sys
from collections import OrderedDict

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../data/questionaire.csv')

# What best describes you?
question = 'What best describes you?'
df[question][18] = 'Other'  # I am a frankenstein of appointments.
plt.figure(figsize=(8, 3))
df[question].value_counts().plot(kind='bar', rot=0)
#cnt = df[question].value_counts()
#plt.figure(figsize=(10, 5))
#plt.bar(cnt.index, cnt.values)
if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/describes_you.png')
    plt.close()
else:
    plt.title(question)
    plt.show()


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
plt.figure(figsize=(10, 3))
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), [k.replace(' ', ' \n ') for k in D.keys()], fontsize="small")
if sys.argv[-1] == '-w':
    plt.savefig('../slides/figs/work_in.png')
    plt.close()
else:
    plt.title(question)
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

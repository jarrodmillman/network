import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data/questionaire.csv')

# What best describes you?
question = 'What best describes you?'
df[question].value_counts().plot(kind='bar')
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

D = dict((field, 0) for field in fields)
for response in df[question]:
    for field in fields:
        if field in response:
            D[field] += 1

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.title(question)
plt.show()


# How often do you?
# will also want to add node information to graphs...
activities = {'Collect data': 'How often do you: [Collect data]',
              'Analyze data': 'How often do you: [Analyze data]',
              'Design methods and algorithms': 'How often do you: [Design methods and algorithms]',
              'Implement algorithms': 'How often do you: [Implement algorithms]',
              'Write scripts': 'How often do you: [Write scripts]',
              'Write software packages': 'How often do you: [Write software packages]'}
freq = ['Never', 'Seldom', 'Sometime', 'Often']
how_often = pd.DataFrame(columns=freq, index=activities)

for k, v in activities.items():
    s = df[v]
    how_often.loc[k] = pd.Series({
        'Never': sum(s == 'Never'),
        'Seldom': sum(s == 'Seldom'),
        'Sometime': sum(s == 'Sometime'),
        'Often': sum(s == 'Often')})

how_often.plot.bar()
plt.show()

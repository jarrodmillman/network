import pandas as pd
import re
import numpy as np

df = pd.read_csv('questionaire.csv')


def column_mapper(column):
    return re.search('\[(.*)\]', column).group(1)


about_person = df[[column for column in df.columns if column.startswith('How do you know')]]
about_person = about_person.rename(columns=column_mapper)

respondent_idx = (about_person == 'It\'s me').values.argmax(axis=1)
respondents = about_person.columns[respondent_idx]

about_person = about_person[respondents]

N = len(respondents)
fields = ('Collaborate',
          'Personally communicate',
          'Use their software',
          'Use their data',
          'Use their algorithm',
          'Familiar with their work',
          'Don\'t know them')
graphs = np.zeros((N, N, len(fields)))

print('Row labels:', respondents)
print('Column labels:', about_person.columns)

for n, person in enumerate(about_person):
    print(f'person == {person}')
    responses = about_person[person]

    for (f, field) in enumerate(fields):
        for r, response in enumerate(responses):
            if (field in response):
                graphs[r, n, f] = 1

np.savez('graph.npz', adjacencies=graphs, fields=fields, people=respondents,
         row_label='Respondent', column_label='Participant')

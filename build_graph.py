import pandas as pd
import re
import numpy as np

df = pd.read_csv('data/Preworkshop questionaire.csv')

def column_mapper(column):
    return re.search('\[(.*)\]', column).group(1)

people = df[[column for column in df.columns if column.startswith('How do you know')]]
people = people.rename(columns=column_mapper)

respondent_idx = (people == 'It\'s me').values.argmax(axis=1)
respondents = people.columns[respondent_idx]

N = len(people.columns)
M = len(respondents)
fields = ('Collaborate', 'Personally communicate', 'Don\'t know them')
collaborations = np.zeros((M, N, len(fields)))

print('Row labels:', respondents)
print('Column labels:', people.columns)

for person in people:
    print(f'person == {person}')
    responses = people[person]

    for (index, field) in enumerate(fields):
        for response in responses:
            pass

print(collaborations.shape)

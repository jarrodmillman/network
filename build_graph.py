import pandas as pd
import re
import numpy as np

df = pd.read_csv('data/Preworkshop questionaire.csv')

def column_mapper(column):
    return re.search('\[(.*)\]', column).group(1)

people = df[[column for column in df.columns if column.startswith('How do you know')]]
people = people.rename(columns=column_mapper)

N = len(people.columns)
fields = ('Collaborate', 'Personally communicate', 'Don\'t know them')
collaborations = np.zeros((N, N, len(fields)))

respondent_idx = (people == 'It\'s me').values.argmax(axis=1)
respondents = people.columns[respondent_idx]
print('respondents:', respondents)

for person in people:
    print(f'person == {person}')
    responses = people[person]

#    if (person_idx == 0) and (person != 'Jarrod Millman'):
#        person_idx = -1

    for (index, field) in enumerate(fields):
        for response in responses:
            pass

print(collaborations.shape)

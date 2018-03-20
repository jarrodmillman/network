import pandas as pd
import re
import numpy as np

df = pd.read_csv('data/Preworkshop questionaire.csv')

def column_mapper(column):
    return re.search('\[(.*)\]', column).group(1)

people = df[[column for column in df.columns if column.startswith('How do you know')]]
people = people.rename(columns=column_mapper)

N = len(people.columns)
collaborations = np.zeros((N, N))

print(collaborations.shape)

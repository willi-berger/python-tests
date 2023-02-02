'''
Tutorial 2 
"How to read and write tabular data"
'''

import pandas as pd

titanic = pd.read_csv('/home/willie/dev/data-files/train.csv')

print(titanic.head(8))

above_70 = titanic[titanic["Age"] > 70]

print(above_70)
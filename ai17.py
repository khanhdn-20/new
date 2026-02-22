import pandas as pd
a = pd.read_csv('student.csv')

print(a.isnull().sum(), '\n')
b = a.fillna(0)
print(b.isnull().sum(), '\n')

print(a.groupby('gender').agg({'math.grade': 'mean', 'sciences.grade': 'sum'}), '\n')

a['a.age'] = a['age'].apply(lambda x: x+2 if x>18 else x-1)
a['total'] = a['english.grade'] + a['math.grade'] + a['sciences.grade'] + a['language.grade']
print(a.head(5))
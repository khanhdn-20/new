import pandas as pd
fi = pd.read_csv('student.csv')
print(fi.head(), '\n-------------------------------')
print(fi.info(), '\n-------------------------------')
print(fi.describe(),'\n-------------------------------')
print(fi.shape, "\n-------------------------------")
print(fi.columns, "\n-------------------------------")
print(fi.dtypes, '\n-------------------------------')
print(fi.loc[0, 'id'], '\n-------------------------------')
print(fi.iloc[1,1], '\n-------------------------------')
print(fi.at[0, 'name'], '\n-------------------------------')
print(fi[fi['language.grade']>4.0], '\n-------------------------------')

fi["med"] = fi['language.grade'] + fi['sciences.grade']
print(fi['sciences.grade'])
print(fi['language.grade'])
print(fi, '\n-------------------------------')

fi = fi.drop(columns = ['med'])
# fi.drop(columns = ['med'], inplace=True)
print(fi)
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

d1 = pd.read_csv('student.csv')
d2 = pd.read_csv('patient.csv')
d = pd.merge(d1, d2, on = 'id', how ='inner') #Gom ca print
# print(d.head(5), '\n')

# print(d1.pivot_table(values= 'math.grade', index= 'nationality', columns= 'gender', aggfunc= 'sum'), '\n')6

d1.plot(kind='bar')
plt.show()
d1['age'].hist()
plt.show()
d3 = d1[['english.grade','math.grade','sciences.grade','language.grade']]
sns.heatmap(d3.corr(numeric_only=True))
plt.show()
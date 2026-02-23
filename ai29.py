import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

d = sns.load_dataset('titanic')
fig, axes = plt.subplots(1,1,figsize=(10,5))

print(d.info())
print(d.describe(include='all'))
# d.drop('deck', axis=1, inplace=True)
d['age'] = d['age'].fillna(0)
print(d.isna().sum())

# sns.heatmap(d.isnull(), cbar=False, cmap='viridis', ax=axes[0])

# sns.histplot(data=d, x='age',ax=axes[1],kde=True,hue='sex')
# sns.boxplot(data=d, x='age', ax=axes[2],color='red')

d['type'] = d['sex'] + " - class " + d['pclass'].astype(str)
# sns.countplot(data=d, x='survived',hue='type',ax=axes[1], width=0.8)
# sns.barplot(data=d, x='pclass', y='survived', estimator=lambda x: sum(x)/len(x)*100,ax=axes[2])

# sns.violinplot(data=d, x='survived',y='pclass')
# sns.violinplot(data=d,x='survived',y='fare')

# sns.pairplot(d[['age','fare','parch']], hue='parch')
pv = pd.pivot_table(data=d,values='fare',index='parch',columns='age')
pv = pv.fillna(0)
print(pv)
sns.heatmap(pv, annot=True, cmap='coolwarm')

plt.tight_layout()
plt.legend()
plt.show()
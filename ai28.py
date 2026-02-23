import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

tips = sns.load_dataset("tips")

# fig, axes = plt.subplots(1, 2, figsize=(15,6))
# sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[0])
# axes[0].set_title("Phân bố tổng hóa đơn")
# axes[0].set_xlabel("Tổng hóa đơn ($)")
# axes[0].set_ylabel("Tần suất")
# sns.violinplot(data=tips, x="time", y="total_bill", palette="muted", ax=axes[1])
# axes[1].set_title("Phân bổ hóa đơn theo thời điểm")
# axes[1].set_xlabel("Thời điểm")
# axes[1].set_ylabel("Tổng hóa đơn ($)")

# d = sns.load_dataset("diamonds")
# sns.scatterplot(data=d,x='carat',y='price',hue=d['cut'].astype(str),size='depth',palette='Spectral',alpha=0.5)
# sns.regplot(data=d,x='carat',y='price',line_kws={'color':'#AA0000'})

f = sns.load_dataset("flights")
pv = pd.pivot_table(f,index='year',columns='month')
print(pv)
# print(f.head())
sns.heatmap(pv,annot=True,cmap='coolwarm',center=0)
g = sns.FacetGrid(f, col='year',col_wrap=4,height=3)
g.map(sns.lineplot, 'month', 'passengers')

# print(d.head())
plt.tight_layout()
plt.show()
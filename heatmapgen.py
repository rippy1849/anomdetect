import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nci1.csv')
data = data.drop(['type'], axis= 1)
print(data)
number_of_rows = len(data.index)
number_of_columns = len(data.columns)

norm = pd.DataFrame(np.zeros((number_of_rows,number_of_rows)))
#print(l2norm)
offset = 1
dim = 2


for row in range(0,number_of_rows):
    for column in range(offset, number_of_rows):
        rgraph = data.iloc[row]
        cgraph = data.iloc[column]
        entry = 0
        for x in range(0,number_of_columns):
            entry = (rgraph[x]-cgraph[x])**dim
        entry = entry**(1/dim)
        norm.iloc[row,column]=entry
        norm.iloc[column,row]=entry
    offset += 1

        

print(norm)
ax= sns.heatmap(norm, cmap="YlGnBu")
plt.show()
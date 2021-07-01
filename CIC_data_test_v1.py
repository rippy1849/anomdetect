import pandas as pd
import os 
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import DBSCAN_clustering_Methods as DB
import clustering_visualization_Methods as vis


directory = "./shortened_data"
color_set = ['red','darkorange','gold','orange','yellow','lime','cyan','green','turquoise','teal','dodgerblue','blue','purple','pink','black']
explicit_color_map = []


data = pd.DataFrame
datanum=0
for entry in os.scandir(directory):
    if data.empty:
        data = pd.read_csv(entry, header=None).drop(0)
        for item in range(0,len(data.index)):
            explicit_color_map.append(color_set[datanum])
    else:
        new = pd.read_csv(entry, header=None).drop(0)
        data = data.append(new)
        for item in range(0,len(new.index)):
            explicit_color_map.append(color_set[datanum])
        
    
    datanum += 1

data = data.drop(columns=[0,1])
number_of_rows = len(data.index)

print(data)


color_map = []
d_cluster = DB.getDBSCANClusterLabels(data, 5, 5)

#print(max(d_cluster))

# for row in range(0,number_of_rows):
#     color_map.append(color_set[d_cluster[row]])
for row in range(0,number_of_rows):
    if d_cluster[row] == -1:
        color_map.append('black')
    else:
        color_map.append('red')   




tsne_2d = TSNE(n_components=2, perplexity=3) #7,10,11,13,17,19 ,20-22, 27
TCs_2d = pd.DataFrame(tsne_2d.fit_transform(data))

p1 = plt.figure(1)
plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = explicit_color_map)
plt.title('t-SNE, Explicit Coloring')
p2 = plt.figure(2)
plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = color_map)
plt.title('t-SNE, Cluster Coloring, DBSCAN')
plt.show()

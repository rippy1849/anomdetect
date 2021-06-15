import networkx as nx
from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

data = pd.read_csv('nci1.csv')
number_of_rows = len(data.index)
color_map = []
color_set = ['red','blue','yellow','green','orange','purple','black']
# When eps is chosen too small, most data will not be clustered at all --> -1 means labeled for noise
# eps of 1.0025, 1.00275, 1.0028
# min_samples of 2 
cluster_DBSCAN = DBSCAN(eps=.067, min_samples=2).fit(data.drop(['type'], axis= 1))
d_cluster = cluster_DBSCAN.labels_

for row in range(0,number_of_rows):
    color_map.append(color_set[d_cluster[row]])

#Visulization (PCA Algorithm)
pca_3d = PCA(n_components=3)
PCs_3d = pd.DataFrame(pca_3d.fit_transform(data.drop(['type'], axis= 1)))

#Visualization (t-SNE Algorithm)
tsne_2d = TSNE(n_components=2, perplexity=3)
TCs_2d = pd.DataFrame(tsne_2d.fit_transform(data.drop(['type'], axis= 1)))



#ax = plt.axes(projection ="3d")
#ax.scatter3D(PCs_3d.loc[:,0],PCs_3d.loc[:,1],PCs_3d.loc[:,2], color = color_map)
plt.scatter(PCs_3d.loc[:,0],PCs_3d.loc[:,1],c  = color_map)

#bx = plt.axes(projection ="3d")
#bx.scatter3D(TCs_3d.loc[:,0],TCs_3d.loc[:,1], TCs_3d.loc[:,2], color = color_map)
#plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = color_map)

plt.title('PCA Dimension-Representation of DBSCAN Clustering')
plt.show()
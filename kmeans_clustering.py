from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#setup values
data = pd.read_csv('nci1.csv')
number_of_rows = len(data.index)
number_of_clusters = 5
color_map = []
color_set = ['red','blue','yellow','green','orange','purple']

#Cluster Algorithm
kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(data.drop(['type'], axis= 1))
k_cluster = kmeans.labels_



#set up color map based on cluster
for row in range(0,number_of_rows):
    color_map.append(color_set[k_cluster[row]])


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


plt.title('PCA Dimension-Representation of Kmeans Clustering')
plt.show()
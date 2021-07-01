import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering


CIC_data_folder = "./shortened_data"





color_map = []
color_map_explicit = []
color_set = ['red','blue','yellow','green','orange','purple','lawngreen','magenta','cyan','darkviolet','plum','mediumturquoise','springgreen','lightcoral','gold','aquamarine','darkcyan','royalblue','slategrey','indigo','olivedrab','blueviolet','palegreen','peru','chocolate','firebrick','wheat','salmon','turquoise','black']
data = pd.DataFrame()
datanum = 0
for entry in os.scandir(CIC_data_folder):
    #data = data.append(pd.read_csv(entry, header=None).drop(columns=[0,1]), ignore_index=True)
    if data.empty:
        data = pd.read_csv(entry, header=None).drop([0])
    else:
        data = data.append(pd.read_csv(entry, header=None).drop([0]), ignore_index=True)
    for row in range(0,len(pd.read_csv(entry, header=None).drop([0]).index)):
        color_map_explicit.append(color_set[datanum])
    datanum +=1
data = data.drop(columns=[0,1])
print(data)

number_of_rows = len(data.index)




number_of_clusters = 2

# kmeans = KMeans(n_clusters=number_of_clusters).fit(data)
# k_cluster = kmeans.labels_
# agglomerativeCluster = AgglomerativeClustering(n_clusters=number_of_clusters).fit(data)
# a_cluster = agglomerativeCluster.labels_
cluster_DBSCAN = DBSCAN(eps=4, min_samples=5).fit(data)
d_cluster = cluster_DBSCAN.labels_
print(max(d_cluster))
#print(d_cluster)


#set up color map based on cluster
for row in range(0,number_of_rows):
    color_map.append(color_set[d_cluster[0]])


#Visulization (PCA Algorithm)
pca_3d = PCA(n_components=3)
PCs_3d = pd.DataFrame(pca_3d.fit_transform(data))

#Visualization (t-SNE Algorithm)



tsne_2d = TSNE(n_components=2, perplexity=3) #7,10,11,13,17,19 ,20-22, 27
TCs_2d = pd.DataFrame(tsne_2d.fit_transform(data))
    
    
# bx = plt.axes(projection ="3d")
# bx.scatter3D(TCs_2d.loc[:,0],TCs_2d.loc[:,1], TCs_2d.loc[:,2], color = color_map)
    
    
# plt.title("stuff")
# plt.show()

#ax = plt.axes(projection ="3d")
#ax.scatter3D(PCs_3d.loc[:,0],PCs_3d.loc[:,1],PCs_3d.loc[:,2], color = color_map)
#plt.scatter(PCs_3d.loc[:,0],PCs_3d.loc[:,1],c  = color_map)


#cx = plt.axes(projection ="3d")
#cx.scatter3D(TCs_2d.loc[:,0],TCs_2d.loc[:,1], TCs_2d.loc[:,2], color = color_map_explicit)
p1 = plt.figure(1)
plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = color_map_explicit)
plt.title('t-SNE, Explicit Coloring')
p2 = plt.figure(2)
plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = color_map)
plt.title('t-SNE, Cluster Coloring, DBSCAN')
plt.show()
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
import DBSCAN_clustering_Methods
import kmeans_clustering_Methods
import agglomerative_clustering_Methods 

def generateColorMap(clusterLabelArray, numDataPoints, color_set):
    # Set up color map based on cluster
    color_map = []
    for row in range(0,numDataPoints):
        color_map.append(color_set[clusterLabelArray[row]])
    return color_map

def generatePCA_Visualization2D(data, color_map):
    #Visualization (PCA Algorithm)
    pca_2d = PCA(n_components=3)
    PCs_2d = pd.DataFrame(pca_2d.fit_transform(data))
    plt.scatter(PCs_2d.loc[:,0],PCs_2d.loc[:,1],c  = color_map)
    plt.title('PCA 2 Dimension-Representation of ... Clustering')
    plt.show()

def generatePCA_Visualization3D(data, color_map):
    pca_3d = PCA(n_components=3)
    PCs_3d = pd.DataFrame(pca_3d.fit_transform(data))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(PCs_3d.loc[:,0],PCs_3d.loc[:,1],PCs_3d.loc[:,2], color = color_map)
    plt.title('PCA 3 Dimension-Representation of ... Clustering')
    plt.show()

def generateTSNE_Visualization2D(data, color_map):
    #Visualization (t-SNE Algorithm)
    tsne_2d = TSNE(n_components=2, perplexity=3)
    TCs_2d = pd.DataFrame(tsne_2d.fit_transform(data))
    p1 = plt.scatter(TCs_2d.loc[:,0],TCs_2d.loc[:,1],c  = color_map)
    #plt.title('TSNE 2 Dimension-Representation of ... Clustering')
    #plt.show()
    return p1

def generateTSNE_Visualization3D(data, color_map):
    tsne_3d = TSNE(n_components=2, perplexity=3)
    TCs_3d = pd.DataFrame(tsne_3d.fit_transform(data))
    bx = plt.axes(projection ="3d")
    bx.scatter3D(TCs_3d.loc[:,0],TCs_3d.loc[:,1], TCs_3d.loc[:,1], color = color_map)
    plt.title('TSNE 3 Dimension-Representation of ... Clustering')
    plt.show()
    
def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    data = data.drop(['type'], axis= 1)
    
    numDataPoints = len(data.index)    
    color_set = ['red','blue','yellow','green','orange','purple']
    
    number_of_clusters = 5
    eps = 1.00275
    min_samples = 2 
    
    cluster_DBSCAN_Labels = DBSCAN_clustering_Methods.getDBSCANClusterLabels(data, eps, min_samples)
    agglomerativeClusterLabels = agglomerative_clustering_Methods.getAgglomerativeClusterLabels(data,number_of_clusters)
    kmeansClusterLabels = kmeans_clustering_Methods.getKMeansClusterLabels(data, number_of_clusters)
    
    color_map = generateColorMap(kmeansClusterLabels, numDataPoints, color_set)
    generatePCA_Visualization2D(data, color_map)
#     generatePCA_Visualization3D(data, color_map, cluster_type)
#     generateTSNE_Visualization2D(data, color_map, cluster_type)
#     generateTSNE_Visualization3D(data, color_map, cluster_type)


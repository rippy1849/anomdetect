from sklearn.cluster import AgglomerativeClustering
import pandas as pd

def getAgglomerativeClusterLabels(data, numClusters):
    # Generate agglomerative cluster
    agglomerativeCluster = AgglomerativeClustering(n_clusters=numClusters).fit(data)
    # Get agglomerative cluster labels 
    agglomerativeClusterLabels = agglomerativeCluster.labels_
    return agglomerativeClusterLabels

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    data = data.drop(['type'], axis= 1)    
    # Get results for agglomerative clustering algorithm
    agglomerativeClusterLabels = getAgglomerativeClusterLabels(data, 5)
    print("Agglomerative Clustering Labels:", agglomerativeClusterLabels)
    
main()
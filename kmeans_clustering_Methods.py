from sklearn.cluster import KMeans
import pandas as pd

def getKMeansClusterLabels(data, numClusters):
    # Generate DBSCAN cluster
    kmeansCluster = KMeans(n_clusters=numClusters, random_state=0).fit(data)
    # Get DBSCAN cluster labels 
    kmeansClusterLabels = kmeansCluster.labels_
    return kmeansClusterLabels

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    data = data.drop(['type'], axis= 1)    
    # Get results for DBSCAN clustering algorithm
    kmeansClusterLabels = getKMeansClusterLabels(data, 5)
    # When eps is chosen too small, most data will not be clustered at all --> -1 means labeled for noise
    print("K-Means Clustering Labels:", kmeansClusterLabels)
    
main()
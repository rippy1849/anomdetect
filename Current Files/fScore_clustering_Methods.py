from sklearn.metrics import f1_score
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import pandas as pd

def getFScoreforDBSCAN(data, y_pred):
    # Run DBSCAN clustering algorithm
    cluster_DBSCAN = DBSCAN(eps=1.00275, min_samples=2).fit(data)
    # Label output for each cluster
    y_true_DBSCAN = cluster_DBSCAN.labels_
    # Run F-Score on cluster array
    fScore_DBSCAN = f1_score(y_true_DBSCAN, y_pred, average='macro')
    return fScore_DBSCAN
    
def getFScoreforKmeans(data, y_pred):
    # Run K means clustering algorithm
    kmeans = KMeans(n_clusters=5, random_state=0).fit(data)
    # Label output for each cluster
    y_true_kmeans = kmeans.labels_
    # Run F-Score on cluster array
    fScore_kmeans = f1_score(y_true_kmeans, y_pred, average='macro')
    return fScore_kmeans

def getFScoreforAgglomerativeClustering(data, y_pred):
    # Run Agglomerative clustering algorithm
    agglomerativeCluster = AgglomerativeClustering(n_clusters=5).fit(data)
    # Label output for each cluster
    y_true_agglomerative = agglomerativeCluster.labels_
    # Run F-Score on cluster array
    fScore_agglomerative = f1_score(y_true_agglomerative, y_pred, average='macro')
    return fScore_agglomerative

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    # Array with predicted output
    y_pred = [0,0,3,3,4,4,4,0,1,1,1,2,2,2,3]
    
    # Get results for F-Score on three clustering algorithms
    fScore_DBSCAN = getFScoreforDBSCAN(data, y_pred)
    fScore_kmeans = getFScoreforKmeans(data, y_pred)
    fScore_agglomerative = getFScoreforAgglomerativeClustering(data, y_pred)
    
    # Results between 0 (no mutual information) and 1 (perfect correlation)
    print("F-Score for DBSCAN:", fScore_DBSCAN)
    print("F-Score for K Means:", fScore_kmeans)
    print("F-Score for Agglomerative Clustering:", fScore_agglomerative)

main()
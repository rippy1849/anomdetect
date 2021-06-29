from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import pandas as pd

def getScoreNMIforDBSCAN(data, y_pred):
    # Run DBSCAN clustering algorithm
    cluster_DBSCAN = DBSCAN(eps=1.00275, min_samples=2).fit(data)
    # Label output for each cluster
    y_true_DBSCAN = cluster_DBSCAN.labels_
    # Run NMI on cluster array
    nmiScore_DBSCAN = normalized_mutual_info_score(y_true_DBSCAN, y_pred)
    return nmiScore_DBSCAN
    
def getScoreNMIforKmeans(data, y_pred):
    # Run K means clustering algorithm
    kmeans = KMeans(n_clusters=5, random_state=0).fit(data)
    # Label output for each cluster
    y_true_kmeans = kmeans.labels_
    # Run NMI on cluster array
    nmiScore_kmeans = normalized_mutual_info_score(y_true_kmeans, y_pred)
    return nmiScore_kmeans

def getScoreNMIforAgglomerativeClustering(data, y_pred):
    # Run Agglomerative clustering algorithm
    agglomerativeCluster = AgglomerativeClustering(n_clusters=5).fit(data)
    # Label output for each cluster
    y_true_agglomerative = agglomerativeCluster.labels_
    # Run NMI on cluster array
    nmiScore_agglomerative = normalized_mutual_info_score(y_true_agglomerative, y_pred)
    return nmiScore_agglomerative

def getScoreNMI(cluster_labels, y_pred):
    nmiScore = normalized_mutual_info_score(cluster_labels, y_pred)
    return nmiScore

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    # Array with predicted output
    y_pred = [0,0,3,3,4,4,4,0,1,1,1,2,2,2,3]
    
    # Get results for NMI on three clustering algorithms
    nmiScore_DBSCAN = getScoreNMIforDBSCAN(data, y_pred)
    nmiScore_agglomerative = getScoreNMIforKmeans(data, y_pred)
    nmiScore_kmeans = getScoreNMIforAgglomerativeClustering(data, y_pred)
    
    # Results between 0 (no mutual information) and 1 (perfect correlation)
    print("NMI Score for DBSCAN:", nmiScore_DBSCAN)
    print("NMI Score for K Means:", nmiScore_kmeans)
    print("NMI Score for Agglomerative Clustering:", nmiScore_agglomerative)

main()

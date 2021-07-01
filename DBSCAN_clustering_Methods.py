from sklearn.cluster import DBSCAN
import pandas as pd


def getDBSCANClusterLabels(data, max_distance, min_num_samples):
    # Generate DBSCAN cluster
    cluster_DBSCAN = DBSCAN(eps=max_distance, min_samples=min_num_samples).fit(data)
    # Get DBSCAN cluster labels 
    cluster_DBSCAN_Labels = cluster_DBSCAN.labels_
    return cluster_DBSCAN_Labels

def main():
    # Read in data
    data = pd.read_csv('nci1.csv')
    data = data.drop(['type'], axis= 1)  
    # Select eps and min number of samples for DBSCAN
    eps = 1.00275
    min_samples = 2
    # Get results for DBSCAN clustering algorithm
    cluster_DBSCAN_Labels = getDBSCANClusterLabels(data, eps, min_samples)
    # When eps is chosen too small, most data will not be clustered at all --> -1 means labeled for noise
    print("DBSCAN Clustering Labels:", cluster_DBSCAN_Labels)


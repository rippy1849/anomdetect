from sklearn.cluster import KMeans
import numpy as np
import os
import json
import networkx as nx
import matplotlib.pyplot as plt

input_path = "./dataset"
G = nx.DiGraph()
color_set = ['red','blue','yellow','green','orange','purple']
color_map = []
cluster_group = {}

# for entry in os.scandir(input_path):
#     data = json.load(open(entry))
#     edge_list = data['edges']
#     kmeans = KMeans(n_clusters=3, random_state=0).fit(edge_list)
#     k_cluster = kmeans.labels_
#     entry_number = 0
#     for edge in edge_list:
#         #print(edge)
#         #print(k_cluster[entry_number])
#
#         for node in edge:
#             cluster_group[node] = k_cluster[entry_number]
#
#         G.add_nodes_from(edge)
#         G.add_edges_from([edge])
#         entry_number +=1
# for node in G:
#     print()
#     color_map.append(color_set[cluster_group[node]])
# nx.draw(G,pos=nx.spring_layout(G), node_color=color_map)
# plt.show()
    
   
    

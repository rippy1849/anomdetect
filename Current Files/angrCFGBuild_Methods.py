import json
from angrutils import *
import networkx as nx
import os
from pathlib import Path

# Receives: 
# Returns: 
# Task:
def generateEdgeList(directory, output_path):
    dataNum = 0
    
    base_path = Path(output_path)
    base_path.mkdir
    # Iterate through every file in directory
    for entry in os.scandir(directory):
        proj = angr.Project(entry.path, load_options={'auto_load_libs':False})
    
        cfg = proj.analyses.CFGFast(force_complete_scan=False)
        G = cfg.graph
        
        # Initialize edge list
        edges = {}
        edges['edges'] = []
        edges['features'] = {}
        
        for line in nx.generate_edgelist(G, data=False):
            test = line.split(" ")
            node1 = test[1].split("[")[-1].split("]")[0]
            node2 = test[-1].split("[")[-1].split("]")[0]
            
            temp = []
            try:
                temp.append(int(node1))
            except:
                temp.append(0)
                node1 = 0
            try:
                temp.append(int(node2))
            except:
                temp.append(0)
                node2 = 0
            edges['edges'].append(temp)
           
            if edges['features'].get(int(node1)) == None:
                edges['features'][int(node1)] = edges['features'].get(int(node1), 1)
            else:
                edges['features'][int(node1)] = edges['features'].get(int(node1)) + 1 
            if edges['features'].get(int(node2)) == None:
                edges['features'][int(node2)] = edges['features'].get(int(node2), 1)
            else:
                edges['features'][int(node2)] = edges['features'].get(int(node2)) + 1 
            
        # Add data to a json output file
        with open("{}/{}.json".format(output_path, str(dataNum)), 'w') as outfile:
            json.dump(edges, outfile)
            
        dataNum += 1

def main():
    directory = "./Programs"
    outputPath = "dataset"
    generateEdgeList(directory, outputPath)

main()
import angr
import json
from angrutils import *
import networkx as nx
import matplotlib.pyplot as plt
import os
from pathlib import Path


dataNum = 0

directory = "./Programs"
output_path = "dataset"
base_path = Path(output_path)
base_path.mkdir(exist_ok=True)



for entry in os.scandir(directory):
    proj = angr.Project(entry.path, load_options={'auto_load_libs':False})
#main = proj.loader.main_object.get_symbol("main")
#start_state = proj.factory.blank_state(addr=main.rebased_addr)
#cfg = proj.analyses.CFGEmulated(fail_fast=True)
    cfg = proj.analyses.CFGFast(force_complete_scan=False)
    G = cfg.graph
    #plot_cfg(cfg, "ais3_cfg", asminst=True, remove_imports=True, remove_path_terminator=True)
    #nx.to_edgelist(cfg, "test.edgelist")
    #nx.write_edgelist(cfg.graph, "test.edgelist", data=True)
    #nx.write_adjlist(cfg.graph, "test.adjlist")
    #print("It has %d nodes and %d edges" % (len(cfg.graph.nodes()), len(cfg.graph.edges())))
    edges = {}
    edges['edges'] = []
    edges['features'] = {}
    tmpmx = 0
    
    for line in nx.generate_edgelist(G, data=False):
        test = line.split(" ")
        node1 = test[1].split("[")[-1].split("]")[0]
        node2 = test[-1].split("[")[-1].split("]")[0]
        temp = []
        temp.append(int(node1))
        temp.append(int(node2))
        edges['edges'].append(temp)
        if int(node1)>tmpmx:
            tmpmx = int(node1)
        if int(node2)>tmpmx:
            tmpmx = int(node2)
       
        if edges['features'].get(int(node1)) == None:
            edges['features'][int(node1)] = edges['features'].get(int(node1), 1)
        else:
            edges['features'][int(node1)] = edges['features'].get(int(node1)) + 1 
        if edges['features'].get(int(node2)) == None:
            edges['features'][int(node2)] = edges['features'].get(int(node2), 1)
        else:
            edges['features'][int(node2)] = edges['features'].get(int(node2)) + 1 
        
        
        
    # for i in range(0,tmpmx+1):
    #     edges['features'][i] = 1

    
    with open("{}/{}.json".format(output_path, str(dataNum)), 'w') as outfile:
        json.dump(edges, outfile)
        
    dataNum += 1

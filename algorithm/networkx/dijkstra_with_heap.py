import heapq
import networkx as nx
import random
import time
from networkx.algorithms.shortest_paths.weighted import all_pairs_dijkstra_path_length

import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_weighted_edgelist('dij.edgelist',nodetype=int)
# heapq.heappush(Q,(5,1))
# heapq.heappush(Q,(3,2))
# min_value , arg_min_index = heapq.heappop(Q)
# print(Q)

def my_extract_min(D,X):
    # arg_min = -1
    # min_value = float('inf')
    # for i in range(len(D)):
    #     if D[i] < min_value:
    #         if i in X:
    #             arg_min = i
    #             min_value = D[i]
    min_value_old = 0
    arg_min_index_old = 0
    min_value_old , arg_min_index_old = heapq.heappop(D)
    for _ in range(len(D)):
        min_value , arg_min_index = heapq.heappop(D)
        t = (arg_min_index in X)
        print(X)
        if t:
            print(arg_min_index_old)
            if min_value < min_value_old:
                min_value_old = min_value
                arg_min_index_old = arg_min_index
            



        
    return min_value_old,arg_min_index_old

def dijkstra(s,G):
    X = set()
    Q = []
    weight = []
    result = []
    decided =[]
    heapq.heappush(Q,(0,s))
    for i in range(len(G)):
        X.add(i)
    while X != {}:
        #print(Q)
        min_value , arg_min_index = my_extract_min(Q,X)
        decided.append(arg_min_index)
        print(X)
        X.remove(arg_min_index)
        result.append(arg_min_index)
        Q.clear()
        neigh = [t for t in G.neighbors(arg_min_index)]
        for nodes in neigh:
            weight = G.edges[arg_min_index,nodes]['weight']
            heapq.heappush(Q,(weight + min_value,nodes))
    return result,decided
result,l = dijkstra(0,G)
print(l)
import networkx as nx
import random
import time
from networkx.algorithms.shortest_paths.weighted import all_pairs_dijkstra_path_length

import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_weighted_edgelist('dij.edgelist',nodetype=int)
D = [float('inf')] * nx.number_of_nodes(G)
def my_extract_min(D,X):
    arg_min = -1
    min_value = float('inf')
    for i in range(len(D)):
        if D[i] < min_value:
            if i in X:
                arg_min = i
                min_value = D[i]
    return arg_min

def dijkstra(s,G):
    X = set()
    for i in range(len(G)):
        X.add(i)
    D[s] = 0
    weight = []
    result = []
    arg_min = s
    result.append(s)
    while X != {}:
        if arg_min == -1:
            break
        if arg_min == s:
            pass
        else:
            result.append(arg_min)
            X.remove(arg_min)
        neigh = [t for t in G.neighbors(arg_min)]
        for nodes in neigh:
            weight = G.edges[arg_min,nodes]['weight']
            if D[nodes] == float('inf'):
                D[nodes] = D[arg_min] + weight
            else:
                if D[nodes] > D[arg_min] + weight:
                    D[nodes] = D[arg_min] + weight
        arg_min = my_extract_min(D,X)
        if arg_min != s:
            pass
        else:
            X.remove(arg_min)
    return result
# for i in range(1000,11000,1000):
#     G = nx.fast_gnp_random_graph(i,0.01)
#     D = [float('inf')] * nx.number_of_nodes(G)
#     for (u,v) in G.edges():
#         G.edges[u,v]['weight'] = random.randint(1,100)
#     start = time.time()
#     result = dijkstra(0,G)
#     elapsed_time = time.time() - start
#     nx.write_weighted_edgelist(G,"random_1000.edgelist")
#     print("n = {0}".format(i))
#     print("{0}\n".format(elapsed_time))
result = dijkstra(0,G)
print(result)
"""
n = 1000
0.07480025291442871

n = 2000
0.28125

n = 3000
0.6502664089202881

n = 4000
1.1519207954406738

n = 5000
1.831103801727295

n = 6000
2.3906140327453613

n = 7000
3.298191785812378

n = 8000
4.368292808532715

n = 9000
5.612995862960815
"""

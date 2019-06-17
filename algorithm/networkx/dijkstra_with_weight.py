#%%
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_weighted_edgelist('./test_weight.edgelist',nodetype=int)
D = [float('inf')] * nx.number_of_nodes(G)
#%%
def my_extract_min(D,X):
    arg_min = -1
    min_value = float('inf')
    for i in range(len(D)):
        if D[i] < min_value:
            if i in X:
                arg_min = i
                min_value = D[i]
    return arg_min
#%%

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

#%%
result = dijkstra(0,G)
print(result)
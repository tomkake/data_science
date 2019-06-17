import networkx as nx

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
    X = set(G.nodes)
    D = [float('inf')] * nx.number_of_nodes(G)
    D[s] = 0
    pi = [0] * nx.number_of_nodes(G)
    weight = []
    result = []
    arg_min = s
    result.append(s)
    while X != {}:
        arg_min = my_extract_min(D,X)
        if arg_min == -1:
            break
        result.append(arg_min)
        X.remove(arg_min)
        for nodes in G.neighbors(arg_min):
            if nodes in X:
                weight = G.edges[arg_min,nodes]['weight']
                if D[nodes] > weight:
                    D[nodes] = weight
                    pi[nodes] = arg_min
    return result , pi

def steiner_to_metric(G,R):
    Gr = nx.Graph()
    Gr.add_nodes_from(R)
    path_dict = {}
    for u in R:
        #uを始点とするG上の最短経路長D[]と使用した辺の情報pi
        D , p = dijkstra(u,G)
        for v in R:
            if v !=u:
                Gr.add_edge(u,v,weight=D[v])
                path_dict[(u,v)] = p[v]
    return Gr,path_dict

def restore_shortestpath(u,v,P):
    path = []
    temp = v
    while temp != u:
        parent = P[temp]
        path.append((parent,temp))
        temp = parent
    path.reverse()
    return path

def restore_Steiner_tree(T,path_dict):
    result = set()
    for u,v in T.edges():
        path = restore_shortestpath(u,v,path_dict)
        for i in range(len(path)):
            if path[i][0] < path[i][1]:
                result.add((path[i][0],path[i][1]))
            else:
                result.add((path[i][1],path[i][0]))

    return result
def Steiner(G,R):
    Gr , path_dict = steiner_to_metric(G,R)
    return restore_Steiner_tree(Gr,path_dict)

G = nx.read_weighted_edgelist('./dij.edgelist',create_using=nx.DiGraph(),nodetype=int)
#S = nx.read_edgelist('./st.edgelist',nodetype=int)
G , path = steiner_to_metric(G,[0,1,2])
print(path)
#print(Steiner(G,[0,1,2]))
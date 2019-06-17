from networkx import random_regular_graph
import networkx as nx
import random
n = 10 # 10 nodes
m = 12  # 20 edges

G = random_regular_graph(n, m,seed=12)
G.remove_nodes_from(random.sample(G.nodes(),2))
fh=open("new_test.edgelist",'w')
for edge in G.edges():
        fh.write("{0} {1}\n".format(edge[0],edge[1]))
#%%
import networkx as nx
import matplotlib.pyplot as plt
import queue
import networkx.algorithms.traversal.depth_first_search as depth_first_search1

#%%
G = nx.read_edgelist('./01/test.edgelist',nodetype = int)
#%%
nx.draw_networkx(G)
plt.show()
#%%
def depth_first_search(graph, target):
    S = set()
    empty = False
    print("start stack")
    stack = queue.LifoQueue()
    stack.put(target)
    #S.add(target)
    while (~(empty)):
        if stack.empty():
            break
        target = stack.get()
        if target in S:
            continue
        S.add(target)
        print(target)
        for v in G.neighbors(target):
            if v in S:
                pass
            else:
                stack.put(v)
    print("end")
#%%
depth_first_search(G,3)
#%%
print(list(depth_first_search1.dfs_tree(G,2)))

#%%

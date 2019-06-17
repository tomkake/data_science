#%%
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_edgelist('new_test.edgelist',nodetype=int)
def odd_even_func(Graph_data):
    root_num = Graph_data.degree
    even_num = 0
    odd_num = 0
    for i in range(len(root_num)):
        if root_num[i] % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    print(even_num)
    print(odd_num)
    if even_num == len(root_num):
        return True
    else:
        return False
#%%
print(odd_even_func(G))
nx.draw_networkx(G)
plt.show()


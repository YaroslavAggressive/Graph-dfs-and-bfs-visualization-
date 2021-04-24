import networkx as nwx
import matplotlib.pyplot as plt
from GraphVisual import MyGraph
from GraphDrawer import GraphDrawer
import imageio

G = nwx.MultiGraph()  #  в мульиграфы включается все (кратные ребра, кольца и т. д.)

G.add_node('A')
G.add_node('B')
G.add_node('C')

G.add_edge('A', 'C')
G.add_edge('B', 'A')
# nwx.draw_circular(G,
#          node_color='y',
#          node_size=1000,
#          with_labels=True)
dfs_res = list(nwx.algorithms.traversal.dfs_tree(G, 'C'))
print(dfs_res)
# plt.show()

D = {'A': ['C', 'D'],
     'B': [],
     'C': ['B', 'D'],
     'D': ['A', 'C', 'E'],
     'E': ['A', 'D']}
G = nwx.DiGraph(D)

dfs_res = list(nwx.algorithms.traversal.dfs_tree(G, 'A'))
print(dfs_res)

grph = MyGraph(D)

g_draw = GraphDrawer(G, dfs_res)
result_gif = g_draw.build_visual(2, True)  # второй аргумент - показывать или нет в консоль, как рисуется bfs или dfs

print(len(G.nodes))

import networkx as nwx
from collections import deque


NODE_NOT_VISITED = 'NV'  # indicator of visited node in bfs the algorithm
NODE_VISITED = 'V'  # indicator of non-visited node in bfs algorithm

class Graph(nwx.MultiDiGraph):

    def __post_init__(self):
        if self.graph is None:
            raise TypeError("wrong input of graph data")  # now only such input is supported


class GraphTraversal:

    # auxiliary function for dfs main algo
    @staticmethod
    def dfs_recursive(node, graph, nodes_colors, result):
        nodes_colors.pop(node)
        result.append(node)
        for node_tmp in graph.neighbors(node):
            if node_tmp in nodes_colors:
                GraphTraversal.dfs_recursive(node_tmp, graph, nodes_colors, result)

    @staticmethod
    def DFS(graph: Graph, start_node):  # depth search
        nodes_colors = {node: None for node in graph.nodes()}
        result = []
        GraphTraversal.dfs_recursive(start_node, graph, nodes_colors, result)
        return result

    @staticmethod
    def BFS(graph: Graph, start_node):  # breadth search
        nodes_visited = dict()
        nodes_stack = deque(start_node)
        while nodes_stack:
            curr_node = nodes_stack.popleft()
            if curr_node not in nodes_visited:
                nodes_visited.update({curr_node: None})
            for node in graph.neighbors(curr_node):
                if node not in nodes_visited:
                    nodes_stack.append(node)
        return list(nodes_visited.keys())

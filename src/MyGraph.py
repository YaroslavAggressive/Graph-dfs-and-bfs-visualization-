import networkx as nwx
from collections import deque


class MyGraph:

    def __init__(self, graph: dict):
        if isinstance(graph, dict):
            self.graph = nwx.MultiDiGraph(graph)

    def get_nodes(self):
        return self.graph.nodes

    def get_neighbours(self, node: str):
        return self.graph.neighbors(node)

    def get_edges(self):
        return self.graph.edges()


class GraphTraversal:

    @staticmethod
    def DFS(graph: MyGraph, start_node):  # depth search
        nodes_colors = {node: 'white' for node in graph.get_nodes()}
        result = []

        def dfs_recursive(node: str):
            nodes_colors[node] = 'gray'
            result.append(node)
            for node_tmp in graph.get_neighbours(node):
                if nodes_colors[node_tmp] == 'white':
                    dfs_recursive(node_tmp)

            nodes_colors[node] = 'black'

        dfs_recursive(start_node)

        return result

    @staticmethod
    def BFS(graph: MyGraph, start_node):  # breadth search
        nodes_visited = {node for node in graph.get_nodes()}
        nodes_stack = deque(start_node)
        result = []
        while nodes_stack:
            curr_node = nodes_stack.popleft()
            if curr_node in nodes_visited:
                result.append(curr_node)
                nodes_visited.remove(curr_node)
            for node in graph.get_neighbours(curr_node):
                if node in nodes_visited:
                    nodes_stack.append(node)
        return result

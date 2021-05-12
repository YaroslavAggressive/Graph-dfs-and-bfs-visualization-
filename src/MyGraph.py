import networkx as nwx
from collections import deque


NODE_NOT_VISITED = 'white'  # indicator of node, which not yet used in the algorithm
NODE_IN_PROCESS = 'grey'  # indicator of processing current node with dfs/bfs algorithm
NODE_WORKED = 'black'  # indicator of finish step of dfs/bfs algorithm with current graph node


class Graph(nwx.MultiDiGraph):

    # input_data: dict = None
    #
    def __post_init__(self):
        if self.graph is None:
            raise TypeError("wrong input of graph data")  # now only such input is supported


    #
    # def __init__(self, graph: dict):
    #     if isinstance(graph, dict):
    #         self.graph = nwx.MultiDiGraph(graph)
    #     else:
    #         raise TypeError("wrong input of graph data")


class GraphTraversal:

    @classmethod  # auxiliary function for dfs main algo
    def dfs_recursive(cls, node, graph, nodes_colors, result):
        nodes_colors[node] = NODE_IN_PROCESS
        result.append(node)
        for node_tmp in graph.neighbors(node):
            if nodes_colors[node_tmp] == NODE_NOT_VISITED:
                cls.dfs_recursive(node_tmp, graph, nodes_colors, result)

        nodes_colors[node] = NODE_WORKED

    @staticmethod
    def DFS(graph: Graph, start_node):  # depth search
        nodes_colors = {node: NODE_NOT_VISITED for node in graph.nodes()}
        result = []
        GraphTraversal.dfs_recursive(start_node, graph, nodes_colors, result)
        return result

    @staticmethod
    def BFS(graph: Graph, start_node):  # breadth search
        nodes_visited = {node for node in graph.nodes()}
        nodes_stack = deque(start_node)
        result = []
        while nodes_stack:
            curr_node = nodes_stack.popleft()
            if curr_node in nodes_visited:
                result.append(curr_node)
                nodes_visited.remove(curr_node)
            for node in graph.neighbors(curr_node):
                if node in nodes_visited:
                    nodes_stack.append(node)
        return result

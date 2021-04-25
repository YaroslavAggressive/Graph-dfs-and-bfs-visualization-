import networkx as nwx


class MyGraph:

    def __init__(self, graph: dict):
        if isinstance(graph, dict):
            self.graph = nwx.Graph(graph)
            self.vertices = self.graph.nodes  # двумерная матрица смежности

    def DFS(self, start_node):  # в глубину
        nodes_colors = {node:'white' for node in self.graph.nodes}
        nodes_stack = [start_node]
        result = []

        def dfs_recursive(node: str):
            nodes_colors[node] = 'gray'
            result.append(node)
            for node_tmp in self.graph.neighbors(node):
                if nodes_colors[node_tmp] == 'white':
                    dfs_recursive(node_tmp)

            nodes_colors[node] = 'black'

        dfs_recursive(start_node)

        return result

    def BFS(self, start_node):  # в ширину
        nodes_visited = {node: False for node in self.graph.nodes}
        nodes_stack = [start_node]
        result = []
        while nodes_stack:
            curr_node = nodes_stack.pop(0)
            if not nodes_visited[curr_node]:
                result.append(curr_node)
                nodes_visited[curr_node] = True
            for node in self.graph.neighbors(curr_node):
                if not nodes_visited[node]:
                    nodes_stack.append(node)
        return result

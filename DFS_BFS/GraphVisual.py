from collections import deque
import networkx as nwx
import matplotlib.pyplot as plt

class MyGraph:

    def __init__(self, graph: dict):
        if isinstance(graph, dict):
            self.graph = nwx.MultiGraph(graph)
            self.vertices = self.graph.nodes  # двумерная матрица смежности
            self.graph = graph
        else:
            return None  # в конструктор передан неверный тип данных для построения графа

    def DFS(self, start_node):  #  в глубину
        nodes_visited = {node:False for node in self.graph.nodes}
        nodes_stack = deque(start_node)
        result = []
        while nodes_stack:
            curr_node = nodes_stack.pop()
            if not nodes_visited[curr_node]:
                result.append(curr_node)
                nodes_visited[curr_node] = True
            for node in self.graph.neighbors(curr_node):
                if not nodes_visited[node]:
                    nodes_stack.append(node)
        return result

    def BFS(self, start_node):  #  в ширину
        nodes_visited = {node: False for node in self.graph.nodes}
        nodes_stack = deque(start_node)
        result = []
        while nodes_stack:
            curr_node = nodes_stack.pop()
            result.append(curr_node)
            for node in self.graph.neighbors(curr_node):
                if not nodes_visited[node]:
                    nodes_stack.append(node)
                    nodes_visited[node] = True
        return result

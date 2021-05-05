import pytest
import networkx as nwx
from MyGraph import MyGraph
from GraphDrawer import GraphDrawer
from MyGraph import GraphTraversal


class Case:
    def __init__(self, name: str, test_num: int, input: dict, start_node: str, expected: list):
        self._name = name  #
        self.expected = expected  # required sequence of vertices after bfs/dfs
        self.start_node = start_node  # vertex from where we search in depth / width
        self.input = input  # graph creating
        self.test_num = test_num

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


graph_isolated_vertex = {'A': ['C', 'D'],
                         'B': [],
                         'C': ['B', 'D'],
                         'D': ['A', 'C', 'E'],
                         'E': ['A', 'D']}
G_1 = nwx.MultiDiGraph(graph_isolated_vertex)
res_1 = list(nwx.algorithms.traversal.dfs_tree(G_1, 'A'))

graph_complete = {'A': ['C', 'D', 'B', 'E', 'S'],
                  'B': ['A', 'S', 'D', 'C', 'E'],
                  'C': ['B', 'D', 'A', 'S', 'E'],
                  'D': ['A', 'C', 'E', 'B', 'S'],
                  'E': ['A', 'D', 'S', 'B', 'C'],
                  'S': ['A', 'B', 'C', 'D', 'E']}
G_2 = nwx.MultiDiGraph(graph_complete)
res_2 = list(nwx.algorithms.traversal.dfs_tree(G_2, 'A'))

graph_regular = {'A': [],
                 'B': ['A', 'Y', 'C'],
                 'C': ['B', 'E', 'D'],
                 'D': ['A', 'C', 'E'],
                 'E': ['B', 'Y', 'D'],
                 'Y': ['A', 'B', 'E']}
G_3 = nwx.MultiDiGraph(graph_regular)
res_3 = list(nwx.algorithms.traversal.dfs_tree(G_3, 'A'))

graph_parallel_edges = {'A': ['D'],
                        'B': ['A', 'S', 'S'],
                        'C': ['B', 'D'],
                        'D': ['A', 'A', 'C', 'E'],
                        'E': ['A', 'D']}
G_4 = nwx.MultiDiGraph(graph_parallel_edges)
res_4 = list(nwx.algorithms.traversal.dfs_tree(G_4, 'A'))

graph_loop = {'A': ['C', 'D'],
              'B': ['A', 'S'],
              'C': ['B', 'D'],
              'D': ['B', 'D', 'E'],
              'E': ['A', 'D']}
G_5 = nwx.MultiDiGraph(graph_loop)
res_5 = list(nwx.algorithms.traversal.dfs_tree(G_5, 'A'))

graph_simple = {'A': ['C', 'D'],
                'B': ['A', 'S', 'B'],
                'C': ['B', 'D'],
                'D': ['A', 'C', 'E', 'D', 'D'],
                'E': ['A']}
G_6 = nwx.MultiDiGraph(graph_simple)
res_6 = list(nwx.algorithms.traversal.dfs_tree(G_6, 'A'))

TEST_CASES_FOR_DFS = [
    Case(name='1: graph with isolated vertex dfs test', test_num=1, input=graph_isolated_vertex, start_node='A', expected=res_1),
    Case(name='2: complete graph dfs test', test_num=2, input=graph_complete, start_node='A', expected=res_2),
    Case(name='3: regular graph dfs test', test_num=3, input=graph_regular, start_node='A', expected=res_3),
    Case(name='4: graph with parallel edges dfs test', test_num=4, input=graph_parallel_edges, start_node='A', expected=res_4),
    Case(name='5: graph with loop dfs test', test_num=5, input=graph_loop, start_node='A', expected=res_5),
    Case(name='6: simple graph dfs test', test_num=6, input=graph_simple, start_node='A', expected=res_6)
]


res_1 = list(nwx.algorithms.traversal.bfs_tree(G_1, 'A'))
res_2 = list(nwx.algorithms.traversal.bfs_tree(G_2, 'A'))
res_3 = list(nwx.algorithms.traversal.bfs_tree(G_3, 'A'))
res_4 = list(nwx.algorithms.traversal.bfs_tree(G_4, 'A'))
res_5 = list(nwx.algorithms.traversal.bfs_tree(G_5, 'A'))
res_6 = list(nwx.algorithms.traversal.bfs_tree(G_6, 'A'))

# tests are calculated on the same set of graphs as dfs
TEST_CASES_FOR_BFS = [
    Case(name='7: graph with isolated vertex bfs test', test_num=7, input=graph_isolated_vertex, start_node='A', expected=res_1),
    Case(name='8: complete graph bfs test', test_num=8, input=graph_complete, start_node='A', expected=res_2),
    Case(name='9: regular graph bfs test', test_num=9, input=graph_regular, start_node='A', expected=res_3),
    Case(name='10: graph with parallel edges bfs test', test_num=10, input=graph_parallel_edges, start_node='A', expected=res_4),
    Case(name='11: graph with loop bfs test', test_num=11, input=graph_loop, start_node='A', expected=res_5),
    Case(name='12: simple graph bfs test', test_num=12, input=graph_simple, start_node='A', expected=res_6)
]


@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_breadth_first_search(bfs: Case) -> None:
    graph = MyGraph(bfs.input)
    answer = GraphTraversal.BFS(graph, bfs.start_node)
    # visual = GraphDrawer("test_images")  # rendering the result
    # visual.build_visual(graph.graph, answer, bfs.test_num, False)  # False - do not display rendering
    assert answer == bfs.expected


@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_depth_first_search(dfs: Case) -> None:
    graph = MyGraph(dfs.input)
    answer = GraphTraversal.DFS(graph, dfs.start_node)
    # visual = GraphDrawer("test_images")  # rendering the result
    # visual.build_visual(graph.graph, answer, dfs.test_num, False)  # False - do not display rendering
    assert answer == dfs.expected

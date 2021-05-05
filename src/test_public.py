import pytest
import networkx as nwx
from MyGraph import MyGraph
from GraphDrawer import GraphDrawer
from MyGraph import GraphTraversal
from dataclasses import dataclass


@dataclass
class Case:
    name: str
    test_num: int
    input: dict
    start_node: str
    expected: list

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


graph_isolated_vertex = {'A': ['C', 'D'],
                         'B': [],
                         'C': ['B', 'D'],
                         'D': ['A', 'C', 'E'],
                         'E': ['A', 'D']}

graph_complete = {'A': ['C', 'D', 'B', 'E', 'S'],
                  'B': ['A', 'S', 'D', 'C', 'E'],
                  'C': ['B', 'D', 'A', 'S', 'E'],
                  'D': ['A', 'C', 'E', 'B', 'S'],
                  'E': ['A', 'D', 'S', 'B', 'C'],
                  'S': ['A', 'B', 'C', 'D', 'E']}

graph_regular = {'A': [],
                 'B': ['A', 'Y', 'C'],
                 'C': ['B', 'E', 'D'],
                 'D': ['A', 'C', 'E'],
                 'E': ['B', 'Y', 'D'],
                 'Y': ['A', 'B', 'E']}

graph_parallel_edges = {'A': ['D'],
                        'B': ['A', 'S', 'S'],
                        'C': ['B', 'D'],
                        'D': ['A', 'A', 'C', 'E'],
                        'E': ['A', 'D']}

graph_loop = {'A': ['C', 'D'],
              'B': ['A', 'S'],
              'C': ['B', 'D'],
              'D': ['B', 'D', 'E'],
              'E': ['A', 'D']}

graph_simple = {'A': ['C', 'D'],
                'B': ['A', 'S', 'B'],
                'C': ['B', 'D'],
                'D': ['A', 'C', 'E', 'D', 'D'],
                'E': ['A']}

START_POINT = 'A'
graph_dicts = [graph_isolated_vertex, graph_complete, graph_regular, graph_parallel_edges, graph_loop, graph_simple]
graphs_nwx = []
for dct in graph_dicts:
    graphs_nwx.append(nwx.MultiDiGraph(dct))

test_names_dfs = ['graph with isolated vertex dfs test', 'complete graph dfs test', 'regular graph dfs test',
                  'graph with parallel edges dfs test', 'graph with loop dfs test', 'simple graph dfs test']
results = []

for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.dfs_tree(graph, START_POINT))
    results.append(tmp_res)

TEST_CASES_FOR_DFS = [Case(name=str(i) + ": " + test_names_dfs[i], test_num=i + 1, input=graph_dicts[i], start_node=START_POINT,
                           expected=results[i]) for i in range(len(graph_dicts))]

results.clear()
for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.bfs_tree(graph, START_POINT))
    results.append(tmp_res)

test_names_bfs = ['graph with isolated vertex bfs test', 'complete graph bfs test', 'regular graph bfs test',
                  'graph with parallel edges bfs test', 'graph with loop bfs test', 'simple graph bfs test']

# tests are calculated on the same set of graphs as dfs
TEST_CASES_FOR_BFS = [Case(name=str(i) + ": " + test_names_bfs[i], test_num=i + 1, input=graph_dicts[i], start_node=START_POINT,
                           expected=results[i]) for i in range(len(graph_dicts))]


@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_breadth_first_search(bfs: Case) -> None:
    graph = MyGraph(bfs.input)
    answer = GraphTraversal.BFS(graph, bfs.start_node)
    # visual = GraphDrawer("test_images")  # rendering the result
    # visual.build_visual(graph, answer, False)  # False - do not display rendering
    assert answer == bfs.expected


@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_depth_first_search(dfs: Case) -> None:
    graph = MyGraph(dfs.input)
    answer = GraphTraversal.DFS(graph, dfs.start_node)
    # visual = GraphDrawer("test_images")  # rendering the result
    # visual.build_visual(graph, answer, False)  # False - do not display rendering
    assert answer == dfs.expected

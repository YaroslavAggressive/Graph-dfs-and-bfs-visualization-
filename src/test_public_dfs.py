import pytest
import networkx as nwx
from MyGraph import Graph
from MyGraph import GraphTraversal
from dataclasses import dataclass
from GraphDrawer import GraphDrawer

TEST_NAME_POSTFIX = "test"  # maybe redundant constant
DFS_NAME = "dfs"
BFS_NAME = "bfs"


@dataclass
class TestData:
    test_name: str
    test_input: dict


@dataclass
class Case:
    name: str
    test_num: int
    input: dict
    start_node: str
    expected: list

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


def get_test_cases(graphs: dict, start_point: str, true_res: list, mode: str):  # creating test for dfs and bfs
    if mode == DFS_NAME or mode == BFS_NAME:  # just in case for the future, in script the correct conditions are passed to the function
        return [Case(name=str(iter_num) + ": " + tmp_key + mode + TEST_NAME_POSTFIX, test_num=iter_num + 1,
                     input=graphs.get(tmp_key), start_node=start_point,
                     expected=true_res[iter_num]) for iter_num, tmp_key in enumerate(graphs.keys())]
    else:
        raise NameError("An invalid name of variable value was passed")


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

graphs_data = {'graph with isolated vertex dfs test': graph_isolated_vertex,
               'complete graph': graph_complete,
               'regular graph': graph_regular,
               'graph with parallel edges': graph_parallel_edges,
               'graph with loop': graph_loop,
               'simple graph': graph_simple}  # filling graph data (adjacency list and its class)

graphs_nwx = []  # creating objects of implemented graph classes from networkx for using built-in methods
for key in graphs_data.keys():
    graphs_nwx.append(nwx.MultiDiGraph(graphs_data.get(key)))

results = []  # creating correct result for comparing and checking methods
for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.dfs_tree(graph, START_POINT))
    results.append(tmp_res)

TEST_CASES_FOR_DFS = get_test_cases(graphs_data, START_POINT, results, DFS_NAME)

results.clear()  # creating comparison data again, but now for bfs-algo
for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.bfs_tree(graph, START_POINT))
    results.append(tmp_res)

# tests are calculated on the same set of graphs as dfs
TEST_CASES_FOR_BFS = get_test_cases(graphs_data, START_POINT, results, BFS_NAME)


@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_breadth_first_search(bfs: Case) -> None:
    graph = Graph(bfs.input)
    answer = GraphTraversal.BFS(graph, bfs.start_node)
    # GraphDrawer.build_visual(graph, answer, "test_images", False)  # False - do not display rendering
    assert answer == bfs.expected


@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_depth_first_search(dfs: Case) -> None:
    graph = Graph(dfs.input)
    answer = GraphTraversal.DFS(graph, dfs.start_node)
    # GraphDrawer.build_visual(graph, answer, "test_images", False)  # False - do not display rendering
    assert answer == dfs.expected

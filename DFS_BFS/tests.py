import pytest
import networkx as nwx
from GraphVisual import MyGraph


class Case:
    def __init__(self, name: str, input: dict, start_node: str, expected: list):
        self._name = name  #
        self.expected = expected  # требуемая последовательность вершин после bfs/dfs
        self.start_node = start_node  # вершина откуда ищем в глубину/ширину
        self.input = input  # сам граф

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


G_1 = nwx.MultiGraph({'A': ['C', 'D'],
                      'B': [],
                      'C': ['B', 'D'],
                      'D': ['A', 'C', 'E'],
                      'E': ['A', 'D']})
res_1 = list(nwx.algorithms.traversal.dfs_tree(G_1, 'A'))

G_2 = nwx.MultiGraph({'A': ['C', 'D'],
                      'B': ['A', 'S'],
                      'C': ['B', 'D'],
                      'D': ['A', 'C', 'E'],
                      'E': ['A', 'D']})
res_2 = list(nwx.algorithms.traversal.dfs_tree(G_2, 'A'))

G_3 = nwx.MultiGraph({'A': ['C', 'D'],
                      'B': ['A', 'S'],
                      'C': ['B', 'Y'],
                      'D': ['A', 'C', 'A'],
                      'E': []})
res_3 = list(nwx.algorithms.traversal.dfs_tree(G_3, 'C'))

G_4 = nwx.MultiGraph({'A': ['D'],
                      'B': ['A', 'S'],
                      'C': ['B', 'D'],
                      'D': ['A', 'C', 'E'],
                      'E': ['A', 'D']})
res_4 = list(nwx.algorithms.traversal.dfs_tree(G_4, 'A'))

G_5 = nwx.MultiGraph({'A': ['C', 'D'],
                      'B': ['A', 'S'],
                      'C': ['B', 'D'],
                      'D': ['B', 'B', 'E'],
                      'E': ['A', 'D']})
res_5 = list(nwx.algorithms.traversal.dfs_tree(G_5, 'A'))

G_6 = nwx.MultiGraph({'A': ['C', 'D'],
                      'B': ['A', 'S'],
                      'C': ['B', 'D'],
                      'D': ['A', 'C', 'E'],
                      'E': ['A']})
res_6 = list(nwx.algorithms.traversal.dfs_tree(G_6, 'A'))

TEST_CASES_FOR_BFS = [
    Case(name='№1', input={'A': ['C', 'D'],
                           'B': [],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_1),
    Case(name='№2', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_2),
    Case(name='№3', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'Y'],
                           'D': ['A', 'C', 'E'],
                           'E': []}, start_node='A', expected=res_3),
    Case(name='№4', input={'A': ['D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_4),
    Case(name='№5', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['B', 'B', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_5),
    Case(name='№6', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A']}, start_node='A', expected=res_6)
]


res_1 = list(nwx.algorithms.traversal.bfs_tree(G_1, 'A'))
res_2 = list(nwx.algorithms.traversal.bfs_tree(G_2, 'A'))
res_3 = list(nwx.algorithms.traversal.bfs_tree(G_3, 'C'))
res_4 = list(nwx.algorithms.traversal.bfs_tree(G_4, 'A'))
res_5 = list(nwx.algorithms.traversal.bfs_tree(G_5, 'A'))
res_6 = list(nwx.algorithms.traversal.bfs_tree(G_6, 'A'))

# тесты считаются на том же наборе графов, что и dfs
TEST_CASES_FOR_DFS = [
    Case(name='№1', input={'A': ['C', 'D'],
                           'B': [],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_1),
    Case(name='№2', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_2),
    Case(name='№3', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'Y'],
                           'D': ['A', 'C', 'E'],
                           'E': []}, start_node='A', expected=res_3),
    Case(name='№4', input={'A': ['D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_4),
    Case(name='№5', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['B', 'B', 'E'],
                           'E': ['A', 'D']}, start_node='A', expected=res_5),
    Case(name='№6', input={'A': ['C', 'D'],
                           'B': ['A', 'S'],
                           'C': ['B', 'D'],
                           'D': ['A', 'C', 'E'],
                           'E': ['A']}, start_node='A', expected=res_6)
]


@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_count_steps_to_exit(bfs: Case) -> None:
    graph = MyGraph(*bfs.input)
    answer = graph.DFS(*bfs.start_node)
    assert answer == bfs.expected


@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_on_border(dfs: Case) -> None:
    graph = MyGraph(*dfs.input)
    answer = graph.BFS(*dfs.start_node)
    assert answer == dfs.expected

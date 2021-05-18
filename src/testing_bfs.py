from test_data import get_test_cases, Case, graphs_data, START_POINT, BFS_NAME, graphs_nwx
from MyGraph import Graph
from MyGraph import GraphTraversal
from GraphDrawer import GraphDrawer
import pytest
import networkx as nwx

results = []  # creating correct result for comparing and checking methods
for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.bfs_tree(graph, START_POINT))
    results.append(tmp_res)

TEST_CASES_FOR_BFS = get_test_cases(graphs_data, START_POINT, results, BFS_NAME)

@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_breadth_first_search(bfs: Case) -> None:
    graph = Graph(bfs.input)
    answer = GraphTraversal.BFS(graph, bfs.start_node)
    # GraphDrawer.build_visual(graph, answer, "test_images", False)  # False - do not display rendering
    assert answer == bfs.expected
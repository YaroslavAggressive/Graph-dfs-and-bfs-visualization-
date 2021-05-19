from test_data import get_test_cases, Case, graphs_data, START_POINT, DFS_NAME, graphs_nwx
from MyGraph import Graph
from MyGraph import GraphTraversal
from GraphDrawer import GraphDrawer
import pytest
import networkx as nwx

results = []  # creating correct result for comparing and checking methods
for graph in graphs_nwx:
    tmp_res = list(nwx.algorithms.traversal.dfs_tree(graph, START_POINT))
    results.append(tmp_res)

TEST_CASES_FOR_DFS = get_test_cases(graphs_data, START_POINT, results, DFS_NAME)

@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_depth_first_search(dfs: Case) -> None:
    graph = Graph(dfs.input)
    answer = GraphTraversal.DFS(graph, dfs.start_node)
    # GraphDrawer.build_visual(graph, answer, "test_images", False)  # False - do not display rendering
    assert answer == dfs.expected

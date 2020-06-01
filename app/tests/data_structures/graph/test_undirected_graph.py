from data_structures.graph.undirected_graph import UndirectedGraph


def test_graph():
    graph = UndirectedGraph()
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(7)
    graph.add_edge(4, 5)
    graph.add_edge(5, 7)

    assert graph.get_connected_nodes(5) == [4, 7], "5 should be connected to 4 and 7"
    assert graph.get_connected_nodes(7) == [5], "7 should be connected to 5"
    
from data_structures.graph.directed_graph import DirectedGraph


def test_graph():
    graph = DirectedGraph()
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(7)
    graph.add_edge(4, 5)
    graph.add_edge(5, 7)

    assert graph.get_connected_nodes(5) == [7], "5 should be connected to 7"
    
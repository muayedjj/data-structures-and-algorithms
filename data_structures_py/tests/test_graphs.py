import pytest

from data_structures_py.graphs.graphs import Queue, Vertex, Edge, Graph


def test_instantiate():
    graph = Graph()
    assert graph


# Node can be successfully added to the graph
def test_add_node_and_size():
    graph = Graph()
    graph.add_node(10)

    actual = 1
    expected = graph.size()

    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()
    n10 = graph.add_node(10)
    n11 = graph.add_node(11)

    graph.add_edge(n10, n11, 1000)

    actual = (10, 11, 1000)
    expected = (
        graph._Graph__adj_list[n11][0].vertex.value,
        graph._Graph__adj_list[n10][0].vertex.value,
        graph._Graph__adj_list[n10][0].weight
    )

    assert actual == expected


# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes(graph_1):
    actual = graph_1[0].get_nodes()
    expected = ['A', 'B', 'E', 'C', 'D']

    assert actual == expected


# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_get_neighbors(graph_1):
    actual = graph_1[0].get_neighbors(graph_1[1])
    expected = [('B', 1), ('C', 2), ('D', 3), ('E', 4)]

    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_size(graph_1):
    actual = graph_1[0].size()
    expected = 5

    assert actual == expected


# A graph with only one node and edge can be properly returned-- HUH/Nani?!!

# An empty graph properly returns null
def test_empty():
    graph = Graph()

    actual = graph.__str__()
    expected = 'Null'

    assert actual == expected


def test_breadth_first(graph_1):
    actual = graph_1[0].breadth_first(graph_1[2])
    expected = ['D', 'A', 'C', 'E', 'B']

    assert actual == expected


def test_depth_first(graph_1):
    actual = graph_1[0].depth_first(graph_1[1])
    expected = ['A', 'B', 'C', 'D', 'E']

    assert actual == expected


@pytest.fixture
def graph_1():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b, 1)
    g.add_edge(a, c, 2)
    g.add_edge(a, d, 3)
    g.add_edge(a, e, 4)
    g.add_edge(c, d, 5)
    g.add_edge(d, e)

    return [g, a, d]

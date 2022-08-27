import pytest

from data_structures_py.graphs.graph_business_trip import business_trip_4
from data_structures_py.graphs.graph import Graph, Edge, Vertex, Queue


def test_business_trip():
    g = Graph()
    a = g.add_node('Metroville')
    b = g.add_node('Pandora')
    c = g.add_node('Arendelle')
    d = g.add_node('New Monstropolis')
    e = g.add_node('Naboo')
    e = g.add_node('Narnia')
    g.add_edge(a, b, 1)
    g.add_edge(a, c, 2)
    g.add_edge(a, d, 3)
    g.add_edge(a, e, 4)
    g.add_edge(c, d, 5)
    g.add_edge(d, e)

    actual = business_trip_4(g, ['Metroville', 'Arendelle', 'Naboo'])

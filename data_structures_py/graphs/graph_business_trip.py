from data_structures_py.graphs.graph import Graph, Edge, Vertex, Queue


def business_trip(gr, arr: list):
    # gr = Graph()
    cost = 0
    trip = 0
    total_cost = 0
    for i in range(len(arr) - 1):
        destination = arr[i + 1]
        if destination in gr.get_neighbors(arr[i]):
            city = arr[i]
            for edge in gr[city]:
                if str(edge[0]) == destination:
                    trip = edge[1]
            cost += trip
        total_cost += cost

    return total_cost


def business_trip_2(gr, arr: list):
    cost = 0
    trip = 0
    total_cost = 0
    for i in range(len(arr) - 1):
        city = arr[i]
        destination = arr[i + 1]
        # if destination in gr.get_neighbors(arr[i]):
        home = gr._Graph__adj_list[city][0].vertex.value
        print(home)

        neighbors = gr._Graph__adj_list.get(city)
        print(neighbors)
        # for k in range(len(neighbors)):
        #     edge = neighbors[k]
        #     if edge[0] == destination:
        #         trip = edge[1]
        # cost += trip
    total_cost += cost

    return total_cost


def business_trip_3(gr=None, arr: list = None):
    adj_list = list(gr.adj_list.items())
    keys = [str(item) for item in gr.adj_list.keys()]

    return keys


def business_trip_4(gr=None, arr: list = None):
    arr.append('Nada')
    adj_list = gr.adj_list.items()
    # print(list(adj_list))
    cities = [list(item) for item in adj_list]
    # print(cities

    start = ''
    destination = ''
    city_names = []
    # trips = []
    axc = []

    k = 0
    cost = 0
    for i in range(len(cities)):
        cities[i][0] = cities[i][0].value
        cities[i][1] = [(item.vertex.value, item.weight) for item in cities[i][1]]
    # print(cities)
    city_names = [city[0] for city in cities]
    # trips = [city[1] for city in cities]
    # print(city_names)

    for place in arr:
        k += 1
        if arr[k] != 'Nada':
            start = place
            destination = arr[k]

        else:
            return cost

        if start not in city_names:
            return 'Null'

        for city in cities:
            for trips in city[1]:
                if trips[0] == destination:
                    print(cost)
                    cost += trips[1]
                    break
    # neighbors = [item.vertex.value for item in cities[i][1]]
    # costs = [item.weight for item in cities[i][1]]

    return cost


g = Graph()
a = g.add_node('A')
b = g.add_node('B')
c = g.add_node('C')
e = g.add_node('E')
d = g.add_node('D')
g.add_edge(a, b, 1)
g.add_edge(a, c, 2)
g.add_edge(a, d, 3)
g.add_edge(a, e, 4)
g.add_edge(c, d, 5)
g.add_edge(d, e)
# print(business_trip_4(g, ['C', 'A', 'E']))
# print(business_trip_4(g, ['A', 'C']))


if __name__ == "__main__":
# g = Graph()
# a = g.add_node('A')
# b = g.add_node('B')
# e = g.add_node('E')
# c = g.add_node('C')
# d = g.add_node('D')
# g.add_edge(a, b, 1)
# g.add_edge(a, c, 2)
# g.add_edge(a, d, 3)
# g.add_edge(a, e, 4)
# g.add_edge(c, d, 5)
# g.add_edge(d, e)

# print(business_trip(g, ['A', 'B']))
# print(g.get_neighbors(a))
    graph2 = Graph()
    pandora = graph2.add_node('pandora')
    arendelle = graph2.add_node('arendelle')
    metroville = graph2.add_node('metroville')
    narina = graph2.add_node('narina')
    naboo = graph2.add_node('naboo')
    manstropolis = graph2.add_node('manstropolis')

    graph2.add_edge(pandora, arendelle, 150)
    graph2.add_edge(arendelle, pandora, 150)
    graph2.add_edge(arendelle, metroville, 99)
    graph2.add_edge(arendelle, manstropolis, 42)
    graph2.add_edge(metroville, pandora, 82)
    graph2.add_edge(metroville, arendelle, 99)
    graph2.add_edge(metroville, manstropolis, 105)
    graph2.add_edge(metroville, naboo, 26)
    graph2.add_edge(metroville, narina, 37)
    graph2.add_edge(narina, metroville, 37)
    graph2.add_edge(narina, naboo, 250)
    graph2.add_edge(naboo, narina, 250)
    graph2.add_edge(naboo, metroville, 26)
    graph2.add_edge(naboo, manstropolis, 73)
    graph2.add_edge(manstropolis, naboo, 73)
    graph2.add_edge(manstropolis, arendelle, 42)
    graph2.add_edge(manstropolis, metroville, 105)

    print(business_trip_4(graph2, ['arendelle', 'manstropolis']))


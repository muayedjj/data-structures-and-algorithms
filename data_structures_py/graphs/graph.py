from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


class Vertex:
    def __init__(self, value):
        """
        Node/vertex constructor
        """
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:

    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        """Add the node to adj_list as key and value it will be an empty list"""
        vertex = Vertex(value)
        self.adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex, weight)
        self.adj_list[start_vertex].append(edge1)
        self.adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        obj_vertices = self.adj_list.keys()
        vertices = []

        for item in obj_vertices:
            vertices.append(item.value)
        return vertices

    def size(self):
        return len(self.adj_list)

    def get_neighbors(self, ver):
        x = self.adj_list.get(ver, [])

        return [(item.vertex.value, item.weight) for item in x]

    def __repr__(self):
        return repr(self.adj_list)

    def __str__(self):
        if not len(self.adj_list):
            return 'Null'

        else:
            return self.__repr__()

    def breadth_first(self, start_vertex):
        """
        Traversal method
        A method that traverses a graph or the part of a graph that is directly or indirectly connected to a starting\
        vertex (input), and returns the values of all values of the vertices traversed in a single python list, ord-\
        ered by their levels of depth in respect to the input/starting vertex.

        param: A vertix in a graph (start_vertex).
        returns: A list (array) of the values of all vertices in the graph so long as they are not islands\
        disconnected from the input (start_vertex).
        """
        result = []
        visited = set()
        q = Queue()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.adj_list.get(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result


if __name__ == "__main__":
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

    print(g.breadth_first(d))

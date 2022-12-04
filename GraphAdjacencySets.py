import abc
import numpy as np


#########################################################################
# The base class representation of a graph with all interface methods
# library abc for Abstract Base Class
#########################################################################

class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


###########################################################################################
# A single node in graph is represented by an adjacency set. Every node has a vertex id.
# Each node is associated with a set of adjacent vertices.
###########################################################################################
class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("The Vertex %d cannot be adjacent to itself" % v)
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


#########################################################################
# The Class "AdjacencySetGraph" represents a graph as an adjacency Set.
# A graph is a list of nodes and each node has a set of adjacent vertices.
# This graph in this current form with below implementation cannot be used to represent weighted edges.
# Only unweighted edges can be represented.
#########################################################################
class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))
        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights >1")
        self.vertex_list[v1].add_edge(v2)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)
        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


#######################################################################################
# Test following sample undirected graph
# 0-----1
# |
# 2-----3
#######################################################################################

g = AdjacencySetGraph(4, directed=False)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))
for i in range(4):
    print("Indegree: ", i, g.get_indegree(i))
for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge Weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()

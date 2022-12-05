from queue import Queue
from Graph import AdjacencyMatrixGraph


def topological_sort(graph: AdjacencyMatrixGraph):
    queue = Queue()
    in_degree_map = {}

    for i in range(graph.num_vertices):
        in_degree_map[i] = graph.get_indegree(i)
        # Queue all nodes which have no dependencies i.e., no edges coming in
        if in_degree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)
        for v in graph.get_adjacent_vertices(vertex):
            in_degree_map[v] = in_degree_map[v] - 1
            if in_degree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This Graph has a Cycle")

    print(sorted_list)


#############################################################################
# Consider below Graph
# 0-----1-----5-----6-----8
#       |         /
#       2-----3
#       |  X
#       4     7
#############################################################################

g = AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(3, 4)
g.add_edge(6, 8)
print('\n===========================================')
print("Adjacent Matrix")
print('===========================================')
g.display()
print('===========================================')
for i in range(g.num_vertices):
    print("for vertex ",i, ":\t", g.get_adjacent_vertices(i), "\t\t\tIn Degree Value:\t", g.get_indegree(i))
print("Topological Sort \n")
topological_sort(g)

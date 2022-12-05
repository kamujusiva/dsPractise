from queue import Queue
from Graph import AdjacencyMatrixGraph


def build_distance_table(graph: AdjacencyMatrixGraph, source):
    # A dictionary mapping from the vertex number to a tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}
    for i in range(graph.num_vertices):
        distance_table[i] = (None, None)
    # The distance to the source from itself is 0
    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)
    while not queue.empty():
        current_vertex = queue.get()
        # the distance of the current vertex from source
        current_distance = distance_table[current_vertex][0]
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # Only update the distance table if no current distance from the source is set
            if distance_table[neighbor][0] is None:
                distance_table[neighbor] = (1 + current_distance, current_vertex)

import networkx as nx
from sys import maxsize as infinite
from simple_queue import *


def bfs_path_length(graph, first_node):
    distance = {}

    for node in graph.nodes():
        distance[node] = infinite

    Q = Queue()
    visited_nodes = [first_node]
    Q.enqueue(first_node)

    distance[first_node] = 0

    while not Q.isEmpty():
        current_node = Q.dequeue()

        for node in graph.neighbors(current_node):
            if node not in visited_nodes:
                visited_nodes.append(node)
                distance[node] = distance[current_node] + 1
                Q.enqueue(node)

    return distance

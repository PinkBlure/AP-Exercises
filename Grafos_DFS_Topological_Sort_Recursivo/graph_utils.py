import networkx as nx


def build_digraph_with_weights():
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.DiGraph()
    for node in range(1, num_nodes + 1):
        graph.add_node(node)

    for edge in range(1, num_edges + 1):
        aux = input().split()
        graph.add_edge(int(aux[0]), int(aux[1]), weight=int(aux[2]))

    return graph

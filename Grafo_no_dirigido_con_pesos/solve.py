import networkx as nx


def build_digraph_with_weights():
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.DiGraph()
    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    for i in range(0, num_edges):
        lines = input().split()
        graph.add_edge(int(lines[0]), int(lines[1]), weight=int(lines[2]))

    return graph

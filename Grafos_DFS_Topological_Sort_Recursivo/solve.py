import networkx as nx


def dfs_topological_sort(graph):
    N = graph.number_of_nodes()

    visibleNodes = set()
    order = {}

    def dfs(u):
        nonlocal N
        visibleNodes.add(u)
        for node in graph.neighbors(u):
            if node not in visibleNodes:
                dfs(node)

        order[u] = N
        N -= 1

        return

    for node in graph.nodes():
        if node not in visibleNodes:
            dfs(node)

    return order

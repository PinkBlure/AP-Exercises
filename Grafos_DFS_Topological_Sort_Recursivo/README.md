# ✨ Project's Title: Grafos: DFS - Topological sort (recursivo) ✨

## Index
- [✨ Project's Title: Grafos: DFS - Topological sort (recursivo) ✨](#-projects-title-grafos-dfs---topological-sort-recursivo-)
  - [Index](#index)
  - [**Project Description**](#project-description)
    - [What does the program do?](#what-does-the-program-do)
    - [Why use Python?](#why-use-python)
    - [Challenges faced while coding](#challenges-faced-while-coding)
    - [How to run the code](#how-to-run-the-code)
  - [**Project Code**](#project-code)
  - [main.py](#mainpy)
  - [solve.py](#solvepy)
  - [graph\_utils.py](#graph_utilspy)
  - [entry\_example.txt](#entry_exampletxt)
---

## **Project Description**
---

### What does the program do?
* This is a program to solve the topological sort using recursion.

### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

### Challenges faced while coding
* Using graph.neighbors(n) gives all the nodes that are connected to node n.

### How to run the code
* Use the main, the solve, and the graph utils. The last one creates a directed graph with weight. Then, add an entry composed as below. 

---
## **Project Code**
---

## main.py
```python
import networkx as nx

from graph_utils import *
from solve import *

graph = build_digraph_with_weights()
assert nx.is_directed_acyclic_graph(graph)

solution = dfs_topological_sort(graph)
d_swap = {v: k for k, v in solution.items()}

print(dict(sorted(d_swap.items())))
```

## solve.py
* In the function we go to the node that doesn't have more nodes assigned, or the node to which all its assigned nodes have been assigned an order, and gave it an order,
```python
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
```

## graph_utils.py
* This is a directed graph with weight from another exercise.
```python
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
```

## entry_example.txt
* The first line is the number of nodes and edges detached by a space.
* The next lines are the edges of the graph composed by the nodes joined and the weight detached by a space.
```txt
8 9
1 4 5
2 4 2
2 5 3
3 5 1
3 8 6
4 6 8
4 7 7
4 8 6
5 7 2
```

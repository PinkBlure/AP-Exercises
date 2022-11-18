# ✨ Project's Title: Grafos: BFS - Shortest path length ✨

### Index
- [✨ Project's Title: Grafos: BFS - Shortest path length ✨](#-projects-title-grafos-bfs---shortest-path-length-)
    - [Index](#index)
  - [### Project Description](#-project-description)
      - [What does the program do?](#what-does-the-program-do)
      - [Why use Python?](#why-use-python)
      - [Challenges faced while coding](#challenges-faced-while-coding)
      - [How to run the code](#how-to-run-the-code)
  - [### Project Code](#-project-code)
    - [main.py](#mainpy)
    - [solve.py](#solvepy)
    - [graph_utils.py](#graph_utilspy)
    - [simple_queue.py](#simple_queuepy)
    - [entry_example.txt](#entry_exampletxt)
---

### Project Description
---

#### What does the program do?
* This is a program to find the shortest path length of a non directed graph.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* Using graph.neighbors(n) gives all the nodes that are connected to node n.

#### How to run the code
* Use the main and the solve for the program and give an entry as descripted below. The repository adds a graph_utils to create a graph, a simple_queue to create a queue for the solve, and a example entry for the program.

---
### Project Code
---

### main.py
```python
import networkx as nx

from graph_utils import *
from solve import *

graph = build_graph()

first_node = 1

distances = bfs_path_length(graph, first_node)
ordered_distances = dict(sorted(distances.items()))
print(ordered_distances)

```

### solve.py
* We fill a dictionary with infinite distances for every node in the graph, that will be our temporal distance.
```python
import networkx as nx
from sys import maxsize as infinite
from simple_queue import *


def bfs_path_length(graph, first_node):
    distance = {}

    for node in graph.nodes():
        distance[node] = infinite
```
* We create a queue to work with the nodes and a list to add the visible nodes of the graph. We insert the first node to start working.
```python
    Q = Queue()
    visited_nodes = [first_node]
    Q.enqueue(first_node)

    distance[first_node] = 0
```
* We visit the neighbors of the current node and if we didn't change the distance of it, we put it in the dictionary.
```python
    while not Q.isEmpty():
        current_node = Q.dequeue()

        for node in graph.neighbors(current_node):
            if node not in visited_nodes:
                visited_nodes.append(node)
                distance[node] = distance[current_node] + 1
                Q.enqueue(node)

    return distance

```

### graph_utils.py
```python
import networkx as nx


def build_graph():
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.Graph()
    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    for i in range(0, num_edges):
        lines = input().split()
        graph.add_edge(int(lines[0]), int(lines[1]))

    return graph
```
### simple_queue.py
```python
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
```

### entry_example.txt
* The first line is the number of nodes and edges detached by a space.
* The next lines are the edges composed by the nodes joined by it detached by a space.
```txt
9 11
1 4
2 8
3 6
4 7
5 2
6 9
7 1
8 5
8 6
9 7
9 3
```

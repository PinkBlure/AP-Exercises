# ✨ Project's Title: Grafo dirigido con pesos ✨

### Index
- [✨ Project's Title: Grafo dirigido con pesos ✨](#-projects-title-grafo-dirigido-con-pesos-)
    - [Index](#index)
  - [### Project Description](#-project-description)
      - [What does the program do?](#what-does-the-program-do)
      - [Why use Python?](#why-use-python)
      - [Challenges faced while coding](#challenges-faced-while-coding)
      - [How to run the code](#how-to-run-the-code)
  - [### Project Code](#-project-code)
    - [main.py](#mainpy)
    - [solve.py](#solvepy)
    - [entry_example.txt](#entry_exampletxt)
---

### Project Description
---

#### What does the program do?
* This is a program to create a directed graph with weight.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* The nodes start in 1 instead of 0.
* When we do the .split(), we say that the arguments are Strings, so when we add the edges, we have to say that they are int to not create new nodes.

#### How to run the code
* Use the main and the solve, and add an entry composed as below.

---
### Project Code
---

### main.py
```python
import networkx as nx
from solve import *

graph = build_digraph_with_weights()

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges(data=True))
```

### solve.py
* First, we start creating a directed graph and adding the nodes.
```python
import networkx as nx


def build_digraph_with_weights():
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.DiGraph()
    for i in range(1, num_nodes + 1):
        graph.add_node(i)
```
* Then, we add the edges, giving an atribbute for the weight.
```python
    for i in range(0, num_edges):
        lines = input().split()
        graph.add_edge(int(lines[0]), int(lines[1]), weight=int(lines[2]))

    return graph
```

### entry_example.txt
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
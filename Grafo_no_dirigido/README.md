# ✨ Project's Title: Grafo no dirigido ✨

### Index
- [✨ Project's Title: Grafo no dirigido ✨](#-projects-title-grafo-no-dirigido-)
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
* This is a program to create a non directed graph.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* We using a .split to detach the inputs. By that, we are saying that the input is a String instead of a numbers, making that in the moment of creating the edges of the graph, it creates new nodes that are the same nodes but being Strings. To solve this, when we insert the edge we make them int the numbers before.
* The nodes start in 1 instead of 0.

#### How to run the code
* Use the main and the solve given. Need to add an entry for the program composed as descripted below.

---
### Project Code
---

### main.py
```python
import networkx  as nx
from solve import *

graph = build_graph()

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())
```

### solve.py
* First, we add the nodes to the graph, so we ensure that no node is left behind by just adding the edges.
```python
import networkx as nx


def build_graph():
    
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.Graph()
    for i in range(1, num_nodes+1):
        graph.add_node(i)
```
* Next, we add the edges of the graph
```python
    for i in range(0, num_edges):
        lines = input().split()
        graph.add_edge(int(lines[0]), int(lines[1]))

    return graph
```

### entry_example.txt
* The first line of the entry is the number of nodes and the number of edges for the graph detached by an space.
* The next lines are the edges for the graph composed by the nodes joined by the edge detached by an space. 

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

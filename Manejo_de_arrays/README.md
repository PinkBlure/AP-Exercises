# ✨ Project's Title: Manejo de arrays ✨

### Index
- [✨ Project's Title: Manejo de arrays ✨](#-projects-title-manejo-de-arrays-)
    - [Index](#index)
  - [### Project Description](#-project-description)
      - [What does the program do?](#what-does-the-program-do)
      - [Why use Python?](#why-use-python)
      - [Challenges faced while coding](#challenges-faced-while-coding)
      - [How to run the code](#how-to-run-the-code)
  - [### Project Code](#-project-code)
    - [main.py](#mainpy)
    - [solve_tsp.py](#solve_tsppy)
    - [entry_example.txt](#entry_exampletxt)
---

### Project Description
---

#### What does the program do?
* This is a program to solve the `genetic algorithm` by `order crossing`.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* The lowerbound is included in the array while upperbound isn't.

#### How to run the code
* Use the main and the solve for the program and add an entry as designed below. The repository includes an entry example.

---
### Project Code
---

### main.py
```python
from solve_tsp import *

string1= input()
parent1 = [int(k) for k in string1.split(',')]

string2= input()
parent2 = [int(k) for k in string2.split(',')]

lower_bound = int(input())
upper_bound = int(input())

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)

print(solution)
```

### solve_tsp.py
* We create an array for the solution, we call it child1.
* First, we take the lower bound and the upper bound and insert the `numbers between them` and append them into child1. If we have an index out of bounds, we append a 0 as a temporal solution.
```python
def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = []

    for i in range(0, len(parent1)):
        if lower_bound <= i < upper_bound:
            child1.append(parent1[i])
        else:
            child1.append(0)
```
* Then, we create an auxiliar `aux` for visiting every position of child1 that has a 0, cause it means that we haven't insert the parent2 number.
* Could happen that the number of parent2 that we want to insert is already in child1, so we have to create another auxiliar `ind` to search the next number of parent2 that is not in child1. Then, we insert it into the first auxiliar.
* Since we are using while loops, and we need to loop back to the beginning when we reach the end of child1, we use `modular arithmetic` to iterate through the loop efficiently.
```python
    aux = upper_bound
    while 0 in child1:
        if child1[aux] == 0:
            if parent2[aux] not in child1:
                child1[aux] = parent2[aux]
            else:
                ind = aux
                while parent2[ind] in child1:
                    ind = (ind + 1) % len(child1)
                child1[aux] = parent2[ind]

        aux = (aux + 1) % len(child1)

    return child1

```

### entry_example.txt
* The first line are the numbers of parent1 detached by a comma.
* The second line are the numbers of parent2 detached by a comma.
* The third one is the lowerbound of parent1.
* The fourth one is the upperbound of parent1.

```txt
8,11,3,5,6,4,2,12,1,9,7,10
1,2,3,4,5,6,7,8,9,10,11,12
6
9
```

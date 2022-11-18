# ✨ Project's Title: Knapsack 0/1 Problem Solved by Memoization ✨

### Index
- [✨ Project's Title: Knapsack 0/1 Problem Solved by Memoization ✨](#-projects-title-knapsack-01-problem-solved-by-memoization-)
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
* This is a program to solve the knapsack problem with 0/1 items and using memoization.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* The program solves the n = 0 element as using the recurrence of max instead of using the recurrence of n < 0.
* Using a key composed by strings and a hyphen solves and assures us that the key will not be repeated and that we will not have no results for the same reason.

#### How to run the code
* Use main and the solve and give it an entry as descripted below. The repository includes an entry example for the program.

---
### Project Code
---

### main.py
```python
from collections import namedtuple
from solve       import *

Item = namedtuple("Item", ['index', 'value', 'weight'])

first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value = solve_memoization(items, capacity)
print(value)
```

### solve.py
* The items are composed by an index assigned in main, the value and the weight given by the input.
```python
from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])
```

* The function creates a dictionary to insert the values of the program.
* `getKey(n, w)`:
  * @param `n` being a pointer initialized in len(items) -1, containing the value of it for the current call.
  * @param `w` being the weight
  * @return String composed by n and w detached by a hyphen.
* `t(n,w)`:
  * @param `n` being a pointer initialized in len(items) -1, containing the value of it for the current call.
  * @param `w` being the weight of n.

* The problem of knapsack 0/1 uses the next recurrence:
  * t(n,w) = t(n-1, w) : `weight of n > w` 
  * t(n,w) = max(t(n-1, w), t(n-1, w - weight of n) + value of n)
  * t(n,w) = 0 : `n <= 0`

```python
def solve_memoization(items, capacity):
    mem = {}

    def getKey(n, w):
        return str(n) + "-" + str(w)

    def t(n, w):
        key = getKey(n, w)

        if key not in mem:
            if n < 0 or w == 0:
                r = 0
            elif items[n].weight > w:
                r = t(n - 1, w)
            else:
                r = max(
                    t(n - 1, w),
                    t(n - 1, w - items[n].weight) + items[n].value
                )

            mem[key] = r
        return mem[key]

    return t(len(items) - 1, capacity)

```


### entry_example.txt
* The entry is a first line composed by the number of items and the maximum capacity of the knapsack detached by an space.
* The next lines are the items that are an option for the knapsack, being composed by the value and the weight of the item detached by an space.

```txt
3 10
45 5
48 8
35 3
```

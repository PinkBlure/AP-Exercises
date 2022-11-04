# ✨ Project's Title: House Robber ✨

### Project Description

#### What does the program do?
* This is a program to do the 'House Robber Problem' by a solver that use 'memoization' and another one that use 'tabulation'.

#### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges facied while coding
* From 'memoization'. Memoization makes the path from the last element to the first using recursion.
* From 'tabulation'. Tabulation makes the path from the first element to the last iteratively.

#### How to run the code
* The program ask for the number of houses in the first line and the rest of lines are the value of every house. A entry example is included in the repository.

### main.py
```python
from solve_memoization import *
from solve_tabulation  import *

first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

value1 = solve_memoization(items)
value2 = solve_tabulation(items)

assert value1 == value2
print(value1)
```

### solve_memoization.py
```python
def solve_memoization(items):
    mem = {}

    def t(n):
        key = n
        if key not in mem:
            if n < 0:
                r = 0
            else:
                r = max(t(n - 2) + items[n], t(n - 1))

            mem[key] = r
        return mem[key]

    return t(len(items) - 1)
```

### solve_tabulation.py
```python
def solve_tabulation(items):
    table = [items[0], max(items[0], items[1])]

    def fill_table():
        for i in range(2, len(items)):
            table.append(max(table[i-2] + items[i], table[i-1]))
        return

    fill_table()

    return table[-1]

```

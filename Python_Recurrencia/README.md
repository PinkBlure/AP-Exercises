# ✨ Project's Title: Python - Recurrencia ✨

## Index
- [✨ Project's Title: Python - Recurrencia ✨](#-projects-title-python---recurrencia-)
  - [Index](#index)
  - [**Project Description**](#project-description)
    - [What does the program do?](#what-does-the-program-do)
    - [Why use Python?](#why-use-python)
    - [Challenges faced while coding](#challenges-faced-while-coding)
    - [How to run the code](#how-to-run-the-code)
  - [**Project Code**](#project-code)
  - [main.py](#mainpy)
  - [solve.py](#solvepy)
  - [entry\_example.txt](#entry_exampletxt)
  - [Credits](#credits)
---

## **Project Description**
---

### What does the program do?
* This is a program to solve the next recurrency.



### Why use Python?
* It uses a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

### Challenges faced while coding
* As I was doing the summation, I realized that I needed to add one at the end, which was not happening because my summation was going from p to q-1. For this, I made the summation go from p to q, so there comes a moment in which p = q and the recursion results in 1 and is added to it.

### How to run the code
* Use the main and the solve added in the repository. Next, add an entry as descripted below.

---
## **Project Code**
---

## main.py
```python
from solve import *

first_line = input().split()
from_value = int(first_line[0])
to_value = int(first_line[1])
step = int(first_line[2])

for i in range(from_value, to_value + 1, step):
    print(solve(i, to_value), end=' ')
print('')
```

## solve.py
* We are doind the exercise with memoization, so we started initializing a dict for the keys and setting how is gonna be the key composed.
```python
def solve(p, q):
    mem = {}

    def getKey(p, q):
        return str(p) + "-" + str(q)
```
* We are going to need a summation, so we created a function for solving it.
```python
    def autoSum(p, q):
        value = 0

        for k in range(p, q):
            value += (t(p, k) + t(k + 1, q))

        return value
```
* Then, we proceed to write the recurrency.
```python
    def t(p, q):
        key = getKey(p, q)

        if key not in mem:
            if p == q:
                r = 1
            else:
                r = max(
                    t(p + 1, q),
                    autoSum(p, q)
                )
            mem[key] = r

        return mem[key]

    return t(p, q)
```

## entry_example.txt
* The first number is the starting value.
* The second number is the ending value.
* The last value is the numbers of steps we need to make into the numbers.
```txt
2 4 2
```
---
## Credits
* https://es.wikipedia.org/wiki/Sumatorio

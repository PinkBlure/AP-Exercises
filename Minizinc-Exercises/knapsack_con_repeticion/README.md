# ✨ Projects's Title: Knapsack ✨

## Project Description

#### What does this program do?
* This is a program to solve knapsack problem with 0..2.

#### Constraints
* Array: taken (indicates the number of times an item is put into the backpack).
* Weight max of capacity.
* Maximize the value.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* Need an entry for n, to define the lenght of the knapsack, has to be an  int.
* Need an entry for capacity, to define the max weight of the knapsack, has to be an int.
* Need an entry for value, to define the values of the items, has to be an array.
* Need an entry for weight, to define the weight of the items, has to be an array.

```minizinc
int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

array[ITEMS] of var 0..2: taken;

constraint sum(i in ITEMS)((weight[i] * taken[i])) <= capacity;

solve maximize sum(i in ITEMS)((value[i] * taken[i]));

output["taken = ", show(taken), "\nTotal Value = ", show(sum(i in ITEMS)((value[i] * taken[i])))];
```

#### Entry example

```txt
3
10
[45,48,35]
[5,8,3]
```

## Credits
* https://www.minizinc.org
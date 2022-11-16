# ✨ Projects's Title: House Robber ✨

## Project Description

#### What does this program do?
* This is a program to solve the house robber problem.

#### Constraints
* Our thief must choose which houses to rob to get the maximum profit.
* So that the alarms do not activate if you steal in a house you cannot steal in the next.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* Need an entry for n, to define the lenght of an array, has to be an int.
* Need an entry for value to define the value of the houses, has to be an array.

```minizinc
int: n;
array[1..n] of int: value;

%Introduzca el código a partir de esta línea

array[1..n] of var 0..1: taken;

constraint forall(i in 1..n-1 where taken[i] == 1)(taken[i+1] != 1);

solve maximize sum(i in 1..n)(taken[i]*value[i]);

output["taken = ", show(taken), "\nTotal Value = ", show(sum(i in 1..n)(taken[i]*value[i]))];
```

#### Entry example

```txt
5
[3,10,3,1,2]
```

## Credits
* https://www.minizinc.org
# ✨ Projects's Title: Array ✨

## Project Description

#### What does this program do?
* This is a program to create an array.

#### Constraints
* The sum of the values ​​in the array is equal to the product of the values ​​in the array.
* The output should be the resulting array.
* The order of the values ​​in the array is increasing .
* x[1] ≤ x[2] … ≤ x[n]
* The goal is to maximize the sum of the values ​​of x.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* Need an entry for n, to define the lenght of an array, has to be an int.

```minizinc
int: n;

array[1..n] of var 1..9: x;

constraint (sum(x) == product(x));
constraint forall (i in 1..n-1) (x[i] <= x[i+1]);

solve maximize sum(x);
```

#### Entry example

```txt
5
```

## Credits
* https://www.minizinc.org
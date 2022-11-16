# ✨ Projects's Title: Sequence ✨

## Project Description

#### What does this program do?
* This is a program to create a sequence.

#### Constraints
* The first value is 0, the last is 3, and the sum of 2 adjacent numbers in the array is 3 at most.
* The value in positions divisible by 3 must be greater than or equal to 2.
* Maximize the sum of the values ​​of the array.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* Need an entry for n, to define the lenght of an array, has to be an int.

```minizinc
int: n;

array[1..n] of var 0..3: x;

constraint x[1] == 0;
constraint x[n] == 3; 
constraint forall(i in 1..n-1)((x[i] + x[i+1]) <= 3);
constraint forall(i in 1..n where i mod 3 == 0)(x[i] >= 2);

solve maximize sum(x);

output["x = \(x)"];
```

#### Entry example

```txt
5
```

## Credits
* https://www.minizinc.org
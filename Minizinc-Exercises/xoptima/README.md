# ✨ Projects's Title: Xoptima ✨

## Project Description

#### What does this program do?
* This is a program to minimize the value of (x-7)^2

#### Constraints
* x has to be divisible by 4.
* Minimize the value of (x-7)^2

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* No need of any entry.

```minizinc
var 0..10: x;
var int: obj = (x-7)^2;

constraint x mod 4 == 0;

solve minimize obj;

output["x= ", show(x), "\nobj=", show(obj)];
```

## Credits
* https://www.minizinc.org
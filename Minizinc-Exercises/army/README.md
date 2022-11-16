# ✨ Projects's Title: Army ✨

## Project Description

#### What does this program do?
* This is a program to make a budget for an army.

#### Constraints
* Maximum budget of 10000$.
* Soldiers from 4 different cities (F, L, Z, J).
* Strength of F: 6, Cost: 13$, 1000 soldiers max.
* Strength of L: 10, Cost: 21$, 400 soldiers max.
* Strength of Z: 8, Cost: 17$, 500 soldiers max.
* Strength of J: 40, Cost: 100$, 150 soldiers max.
* Maximize the strength of the army.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* No need of any entry.

```minizinc
var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

constraint (13*F + 21*L + 17*Z + 100*J) <= 10000;

var int: Total = 6*F + 10*L + 8*Z +40*J;
solve maximize Total;
```

## Credits
* https://www.minizinc.org
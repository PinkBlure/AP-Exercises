# ✨ Projects's Title: Count ✨

## Project Description

#### What does this program do?
* This is a program to find the number of soldiers in an army.

#### Constraints
* The number is between 100 and 500.
* They are arranged in columns of 5 soldiers, with 2 left over.
* They are arranged in columns of 7 soldiers and 2 are left over.
* They are arranged in columns of 12 soldiers, with 1 left over.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* No need of an entry.

```minizinc
var 100..500: army;

constraint army mod 5 == 2;
constraint army mod 7 == 2;
constraint army mod 12 == 1;

solve satisfy;
```

## Credits
* https://www.minizinc.org
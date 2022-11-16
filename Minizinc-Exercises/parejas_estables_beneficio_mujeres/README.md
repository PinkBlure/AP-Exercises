# ✨ Projects's Title: Parejas Estables Beneficio Mujeres ✨

## Project Description

#### What does this program do?
* This is a program to solve stable_matching with preference to women.

#### Constraints
* Maximize the number of women who get their first choice as a men.

#### Why use Minizinc?
* Minizinc is used to model constraint satisfaction and optimization problems in a high-level, solver-independent way, taking advantage of a large library of pre-defined constraints.

#### How to run the program
* Need an input for women, to define the names of the women, has to be an enum.
* Need an input for men, to definethe names of the men, has to be an enum.
* Need an input for wrank, to define the preferences of men from women, has to be an array.
* Need an input for mrank, to define the preferences of women from men, has to be an array.

```minizinc
include "globals.mzn";

enum Women;
enum Men;

array[Women, Men] of int: wrank;
array[Men, Women] of int: mrank;

array[Men] of var Women: wife;
array[Women] of var Men: husband;

constraint inverse(wife, husband);

constraint forall(m in Men, w in Women)(mrank[m,w] < mrank[m,wife[m]] -> wrank[w,husband[w]] < wrank[w,m]);
constraint forall(m in Men, w in Women)(wrank[w,m] < wrank[w, husband[w]] -> mrank[m,wife[m]] < mrank[m,w]);

var int: obj_men = sum(m in Men)(mrank[m, wife[m]] == 1);
var int: obj_women = sum(w in Women)(wrank[w, husband[w]] == 1);

solve maximize obj_women;

output["wife : \(wife)\nhusband: \(husband)\nobj_men:\(obj_men)\nobj_women:\(obj_women)"];
```

#### Entry example

```txt
{Ana, Marta, Patricia}
{Carlos, Marco, Juan}
[|1, 2, 3,|3, 2, 1,|3, 1, 2|]
[|2, 1, 3, |1, 2, 3, |1, 3, 2 |]
```

## Credits
* https://www.minizinc.org
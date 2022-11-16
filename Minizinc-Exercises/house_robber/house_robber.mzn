int: n;
array[1..n] of int: value;

%Introduzca el código a partir de esta línea

array[1..n] of var 0..1: taken;

constraint forall(i in 1..n-1 where taken[i] == 1)(taken[i+1] != 1);

solve maximize sum(i in 1..n)(taken[i]*value[i]);

output["taken = ", show(taken), "\nTotal Value = ", show(sum(i in 1..n)(taken[i]*value[i]))];
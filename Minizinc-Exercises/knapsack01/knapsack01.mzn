int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí

array[ITEMS] of var 0..1: taken;

constraint sum(i in ITEMS)((weight[i] * taken[i])) <= capacity;

solve maximize sum(i in ITEMS)((value[i] * taken[i]));

output["taken = ", show(taken), "\nTotal Value = ", show(sum(i in ITEMS)((value[i] * taken[i])))];
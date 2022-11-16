var 0..10: x;
var int: obj = (x-7)^2;

constraint x mod 4 == 0;

solve minimize obj;

output["x= ", show(x), "\nobj=", show(obj)];
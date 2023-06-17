from math import e
from sympy import *

# função = e^x - tan(x)
a = 1
b = 1.5
c = (a + b) / 2
x = Symbol('x')
fun = atan(e**x)
erro = 10 ** -3
n = 0
x0 = fun.subs(x, c)

while n < 100 and abs(e**x0 - tan(x0)) > erro:
    c = x0
    x0 = fun.subs(x, c)
    print(f'Iteração {n}: {x0}')
    n += 1

print(f'Valor final: {x0}')

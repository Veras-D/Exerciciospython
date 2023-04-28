import sympy
from math import *
x = sympy.symbols('x')
a = sympy.symbols('a')
# (2*((tan({a})-sin({a})))-{a}**3)/{a}**3
fun = f'(sin({a})+1)**0.5'
derv = 0
n = int(input('Insira o n: '))
maclaurin = []
for n in range(0, n + 1):
    if n == 0:
        print(fun)
        maclaurin.append(sympy.sympify(fun) * (x - a) ** n / factorial(n))
    else:
        derv = sympy.diff(fun)
        print(derv)
        maclaurin.append(derv * (x - a) ** n / factorial(n))
        fun = derv
print(maclaurin)
maclaurin_soma = sum(maclaurin).subs({a: 0})
print(maclaurin_soma)
aprox = maclaurin_soma.subs({x: 0})
print(aprox)

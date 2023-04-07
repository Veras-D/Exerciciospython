import sympy
from math import *
x = sympy.symbols('x')
a = sympy.symbols('a')
fun = f'sin({a})'
derv = 0
n = int(input('Insira o n: '))
maclaurin = []
for n in range(0, n + 1):
    derv = sympy.diff(fun)
    print(derv)
    maclaurin.append(derv * x**n / factorial(n))
    n += 1
    fun = derv
print(maclaurin)
maclaurin_soma = sum(maclaurin)
print(maclaurin_soma.subs({a: 0}))

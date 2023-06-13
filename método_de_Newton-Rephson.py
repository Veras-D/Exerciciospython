import sympy
from math import *
from decimal import Decimal, getcontext
getcontext().prec = 50
# X1 = X0 - Y0 / f'(X0)
c = 0
x = sympy.symbols('x')
x0 = Decimal(input('Qual o chute inicial? '))
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 1000  # número máximo de iterações
fun = f'cos({x}) - {x}'
y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))
while abs(y0) > erro and c < n:  # tentar colocar abs(x1 — x0) > erro na condição de repetição, 2 whiles?
    y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))
    dev_y0 = Decimal(str(sympy.diff(fun).subs({x: x0})))
    x1 = x0 - y0 / dev_y0
    a = x0
    x0 = x1
    c += 1  # tentar usar o break
    print(x0)
    print(a - x0)
    print(c)
print(x0)
print(y0)

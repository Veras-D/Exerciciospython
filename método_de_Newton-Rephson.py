import sympy
from math import *
from decimal import Decimal, getcontext
getcontext().prec = 50
# precisa de um ponto, funciona por tangente
# X1 = X0 - Y0 / f'(X0)
c = 0
x = sympy.symbols('x')
x0 = Decimal(input('Qual o chute inicial? '))
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações
fun = f'36 * {x} ** 5 + 432 * {x} ** 4 - 13 * {x} ** 3 + 156 * {x} ** 2 + {x} + 12'
y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))
while abs(y0) > erro and c < n:  # tentar colocar abs(x1 e x0) > erro na condição de repetição, 2 whiles???
    y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))
    dev_y0 = Decimal(str(sympy.diff(fun).subs({x: x0})))
    x1 = x0 - y0 / dev_y0
    x0 = x1
    c += 1
    print(x0)
    print(c)
print(x0)
print(y0)

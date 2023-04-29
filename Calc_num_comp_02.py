import sympy
from math import *
# método Newton-Rephson
# precisa de um ponto, funciona por tangente
# X1 = X0 - Y0 / f'(X0)
c = 0
x = sympy.symbols('x')
x0 = float(input('Qual o chute inicial? '))
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações
# 36 * {x} ** 5 + 432 * {x} ** 4 - 13 * {x} ** 3 + 156 * {x} ** 2 + {x} + 12
fun = f'36 * {x} ** 5 + 432 * {x} ** 4 - 13 * {x} ** 3 + 156 * {x} ** 2 + {x} + 12'
y0 = sympy.sympify(fun).subs({x: x0})
dev_y0 = sympy.diff(fun).subs({x: x0})
x1 = x0 - y0 / dev_y0
y1 = sympy.sympify(fun).subs({x: x1})
print(y1 - y0)
while abs(y1) > erro and c < 100:  # repensar condição de repetição
    y0 = sympy.sympify(fun).subs({x: x0})
    dev_y0 = sympy.diff(fun).subs({x: x0})
    x1 = x0 - y0 / dev_y0
    x0 = x1
    c += 1
    print(x0)
    print(c)
print(x0)
print(y0)

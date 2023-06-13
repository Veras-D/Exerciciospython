from math import *
import sympy
import numpy as np
import matplotlib.pyplot as plt
# tentar usar a função N do sympy para deixar o resultado com mais casa decimais
cod = 0
c = 0
x = sympy.symbols('x')
a = 0.5
b = 1
x0 = (a + b) / 2
num = 3  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações
fun = f'{sympy.cos(x)} - {x}'
f_x0 = sympy.sympify(fun).subs({x: x0})
# x_graf = np.linspace(a, b)
# y = x_graf ** 3 + 12 * x_graf + 14
# plt.plot(x_graf, y)
# plt.grid(True)
# plt.show()
while abs(a - b) > erro and c < n:
    x0 = (a + b) / 2
    f_a = eval(str(sympy.sympify(fun).subs({x: a})))
    f_b = eval(str(sympy.sympify(fun).subs({x: b})))
    f_x0 = eval(str(sympy.sympify(fun).subs({x: x0})))
    print(type(f_a))
    # f(a) * f(b) < 0 tem pelo menos uma raiz
    print(f_x0)
    print(f_a * f_x0)
    print(f_b * f_x0)
    if f_a * f_x0 < 0:
        b = x0
    elif f_b * f_x0 < 0:
        a = x0
    else:
        cod = 1
        break
    c += 1
if cod == 0:
    print(a)
    print(b)
    print(x0)
else:
    print('Não há raiz no intervalo')
# programa da erro se considerar o modulo

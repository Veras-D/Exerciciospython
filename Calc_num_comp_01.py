from math import *
import sympy
import numpy as np
import matplotlib.pyplot as plt
# tentar usar a função N do sympy para deixar o resultado com mais casa decimais
c = 0
x = sympy.symbols('x')
a = -5
b = 15
x0 = (a + b) / 2
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações
fun = f'{x} ** 3 + 12 * {x} + 14'
f_x0 = sympy.sympify(fun).subs({x: x0})
x_graf = np.linspace(a, b)
y = x_graf ** 3 + 12 * x_graf + 14
plt.plot(x_graf, y)
plt.grid(True)
plt.show()
while abs(a - b) > erro and c < n:
    x0 = (a + b) / 2
    f_a = sympy.sympify(fun).subs({x: a})
    f_b = sympy.sympify(fun).subs({x: b})
    f_x0 = sympy.sympify(fun).subs({x: x0})
    # f(a) * f(b) < 0 tem pelo menos uma raiz
    print(f_a * f_x0)
    print(f_b * f_x0)
    if f_a * f_x0 < 0:
        b = x0
    if f_b * f_x0 < 0:
        a = x0
    else:
        print('Não há raiz no intervalo')
        break
    c += 1
print(a)
print(b)
print(x0)
# programa da erro se considerar o modulo

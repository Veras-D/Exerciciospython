from math import *
import sympy
import numpy as np
x = np.linspace(-100, 0, 21)
print(x)
a = 0
b = 10
f = sympy.sympify(input('Qual a função? '))
# while f(y) <= 0.0001 or f(a) <= 0.0001 or f(b) <= 0.0001:
    # y = abs(a + b) / 2
    # f(a) * f(b) < 0 tem pelo menos uma raiz
    # if f(a) * f(y) < 0:
        # b = abs(a + y) / 2
    # if f(b) * f(y) < 0:
        # a = abs(b + y) / 2
    # else
        # print('Não há raiz no intervalo')
# print(a)
# print(b)
# print(y)
# programa da erro se considerar o modulo
from math import *
import sympy
# tentar usar a função N do sympy para deixar o resultado com mais casa decimais
import numpy as np
# para que usar o numpy???, Plotar o grafico???
x = sympy.symbols('x')
a = 0
b = 10
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações
fun = f'{e} ** {x}'
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

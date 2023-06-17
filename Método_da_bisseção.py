from math import *
import sympy
import numpy as np
import matplotlib.pyplot as plt

# Importação de bibliotecas necessárias

cod = 0
c = 0
x = sympy.symbols('x')

a = 1
b = 1.5

x0 = (a + b) / 2
num = 3  # número de casas decimais confiáveis
erro = 10 ** -num
n = 100  # número máximo de iterações

fun = f'{e ** x -  sympy.tan(x)}'

f_x0 = sympy.sympify(fun).subs({x: x0})

if f_x0 <= erro:
    print(f'Valor de x0: {x0}')
else:
    # Loop principal para encontrar a raiz
    while abs(a - b) > erro and c < n:
        x0 = (a + b) / 2

        # Avaliação da função nos pontos a, b e x0
        f_a = eval(str(sympy.sympify(fun).subs({x: a})))
        f_b = eval(str(sympy.sympify(fun).subs({x: b})))
        f_x0 = eval(str(sympy.sympify(fun).subs({x: x0})))

        # Verificação de condições para atualizar os limites do intervalo
        if f_a * f_x0 < 0:
            b = x0

        elif f_b * f_x0 < 0:
            a = x0

        else:
            cod = 1
            break

        c += 1

    # Verificação do resultado
    if cod == 0:
        print(f'Valor de a: {a}')
        print(f'Valor de b: {b}')
        print(f'Valor de x0: {x0}')

    else:
        print('Não há raiz no intervalo')

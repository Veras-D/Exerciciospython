import sympy
from math import *
from decimal import Decimal, getcontext

# Configuração de precisão decimal
getcontext().prec = 50

# Declaração das variáveis e parâmetros iniciais
c = 0
x = sympy.symbols('x')
x0 = Decimal(input('Qual o chute inicial? '))  # Chute inicial fornecido pelo usuário
print(f'Chute inicial: {x0}\n')
num = 7  # número de casas decimais confiáveis
erro = 10 ** -num
n = 1000  # número máximo de iterações

fun = f'{e}**{x} - tan({x})'  # Expressão da função

y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))  # Valor da função no ponto x0

# Loop principal para o método de Newton-Raphson
while abs(y0) > erro and c < n:
    y0 = Decimal(str(sympy.sympify(fun).subs({x: x0})))  # Avaliação da função no ponto x0
    dev_y0 = Decimal(str(sympy.diff(fun).subs({x: x0})))  # Avaliação da derivada da função no ponto x0
    x1 = x0 - y0 / dev_y0  # Cálculo do próximo valor de x usando a fórmula do método de Newton-Raphson
    a = x0  # Armazenamento do valor atual de x0
    x0 = x1  # Atualização do valor de x0 para o próximo loop
    c += 1  # Contador de iterações
    print(F'Iteração número: {c}')  # Número da iteração atual
    print(f'x0: {x0}')
    print(f'Erro: {a - x0}\n')  # Diferença entre o valor atual e o anterior de x0

# Impressão do resultado
print(f'Valor final de x0: {x0}')  # Valor de x encontrado
print(f'Valor final de y0: {y0}')  # Valor da função no ponto x0

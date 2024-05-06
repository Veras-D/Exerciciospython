"""
Caixa
Date: 24/05/06
Author: Veras-D
"""
cedulas = [50, 10, 1]

valor = int(input('Qual o Valor: '))

cel_50 = int(valor // cedulas[0])
cel_10 = int((valor - cel_50 * cedulas[0]) // cedulas[1])
cel_1 = int((valor - cel_10 * cedulas[1] - cel_50 * cedulas[0]) // cedulas[2])

print(f'50: {cel_50}\n10: {cel_10}\n1: {cel_1}')

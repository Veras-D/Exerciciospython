"""
Programa para calcular o fatorial de um número por meio do loop de repetição while
Data: 28/07/23
Autor: Veras-D
"""
import numpy as np
fac = []
num = int(input('Escolha o numero do qual você deseja calcular o fatorial: '))
nums = num
while num > 0:
    fac.append(num)
    num -= 1
fac = np.array(fac).prod()
print(f'O fatorial de {nums} é {fac}.')

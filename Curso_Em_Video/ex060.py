"""
Program to calculate the factorial of a number through the while loop repetition
Date: 07/28/23
Author: Veras-D
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

"""
Programa que calcula a soma de números pares em um conjunto de seis números definidos pelo usuário.
Data: 26/03/22
Author: Veras-D
"""
s = 0
num_soma = 0
for cont in range(1, 7):
    valor = int(input('Digite um valor? '))
    if valor % 2 == 0:
        s += valor
        num_soma += 1
print(f'Dos {cont} valores digitados, {num_soma} foram pares e o resultando de sua soma foi {s}.')

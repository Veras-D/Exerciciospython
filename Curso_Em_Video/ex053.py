"""
Verificador de palíndromo
Data: 29/03/23
Author: Veras-D
"""
teste = 0
contador = 0
a = str(input('Digite seu teste: ')).lower().replace(' ', '')
b = a[::-1]
for cont in range(len(a) - 1, -1, -1):
    if a[cont] != a[contador]:
        teste += 1
    contador += 1
print(f'O inverso de {a} é {b}, portanto', end=' ')
if teste == 0:
    print('é PALÍNDROMO.')
else:
    print('Não é PALÍNDROMO.')

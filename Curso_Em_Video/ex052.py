"""
Identificador de números primos
Data: 28/03/23
Author: Veras-D
"""
import colorama
a = 0
n = int(input('Digite um numero: '))
if n == 1:
    print('1 não é PRIMO')
else:
    print(colorama.Fore.GREEN, 1, colorama.Style.RESET_ALL, end='')
    for cont in range(2, n):
        resto = n % cont
        if resto == 0:
            print(colorama.Fore.GREEN, cont, colorama.Style.RESET_ALL, end='')
            a = 1
        else:
            print(colorama.Fore.RED, cont, colorama.Style.RESET_ALL, end='')
    print(colorama.Fore.GREEN, n, colorama.Style.RESET_ALL)
    if a == 1:
        print(f'{n} não é PRIMO')
    elif a == 0:
        print(f'{n} é PRIMO')

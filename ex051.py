"""
Dez termos de uma PA
Data: 27/03/23
Author: Veras-D"""
a0 = float(input('Qual o primeiro termo da PA? '))
r = float(input('Qual a razão da PA? '))
for cont in range(1, 10):
    an = a0 + r * (cont - 1)
    print(an, end='; ')
print(a0 + r * cont, end=' ')
print('FIM!')

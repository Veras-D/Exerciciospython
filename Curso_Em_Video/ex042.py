"""
Programa para categorizar um triangulo a partir dos seus lados
Data: 05/3/23
Autor: Veras-D
"""
l1 = float(input('Qual o primeiro lado? '))
l2 = float(input('Qual o segundo lado? '))
l3 = float(input('Qual o terceiro lado? '))
if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
    if l1 == l2 and l2 == l3:  # também pode ser escrito como l1 == l2 == l3
        print('EQUILÁTERO')
    elif l1 == l2 and l2 != l3:
        print('ISÓSCELES')
    elif l2 == l3 and l1 != l2:
        print('ISÓSCELES')
    elif l1 == l3 and l1 != l2:
        print('ISÓSCELES')
    elif l1 != l2 and l2 != l3 and l1 != l3:  # também pode ser escrito como l1 != !2 != l3 != l1
        print('ESCALENO')
else:
    print('Não é um triangulo')

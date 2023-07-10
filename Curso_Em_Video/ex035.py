l1 = float(input('Digite o primeiro seguimento do triangulo: '))
l2 = float(input('Digite o segundo seguimento do triangulo: '))
l3 = float(input('Digite o terceiro seguimento do triangulo: '))
if l1 + l2 <= l3:
    print('Esses seguimentos não formam um triangulo.')
elif l2 + l3 <= l1:
    print('Esses seguimentos não formam um triangulo.')
elif l1 + l3 <= l2:
    print('Esses seguimentos não formam um triangulo.')
else:
    print('Esses seguimentos formam um triangulo.')
# podia ter deixado todas as condições em um unico if com o and

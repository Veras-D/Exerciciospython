n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if n1 > n2:
    print(f'{n1:.2f} é maior que {n2:.2f}.')
elif n2 > n1:
    print(f'{n2:.2f} é maior que {n1:.2f}.')
elif n1 == n2:
    print(f'{n1:.2f} é igual a {n2:.2f}.')
else:
    print('Opção não valida.')

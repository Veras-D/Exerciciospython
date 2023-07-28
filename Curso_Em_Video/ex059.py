r = 'S'
num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))
while r == 'S':
    print('[ 1 ] - Somar \n[ 2 ] - Multiplicar \n[ 3 ] - Maior \n[ 4 ] - Novos Números \n[ 5 ] - Sair Do Programa')
    opc = int(input('Opções: '))
    if opc == 1:
        res = num1 + num2
        print(f'A soma de {num1} com {num2} é igual a {res}.')
        r = str(input('Deseja Continuar [S/N]: ')).upper()
    elif opc == 2:
        res = num1 * num2
        print(f'A multiplicação de {num1} com {num2} é igual a {res}.')
        r = str(input('Deseja Continuar [S/N]: ')).upper()
    elif opc == 3:
        if num1 == num2:
            print('Os números escolhidos são iguais, portanto não há maior ou menor')
        elif num1 > num2:
            print(f'O maior número é: {num1}')
        else:
            print(f'O maior número é: {num2}')
        r = str(input('Deseja Continuar [S/N]: ')).upper()
    elif opc == 4:
        num1 = float(input('Numero 1: '))
        num2 = float(input('Numero 2: '))
    elif opc == 5:
        r = 'N'
    else:
        print('Opção invalida tente novamente')
print('Fim do programa.')

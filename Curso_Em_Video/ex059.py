r = 'S'
while r == 'S':
    num1 = float(input('Numero 1: '))
    num2 = float(input('Numero 2: '))
    opc = int(input('Opções: '))
    if opc == 1:
        print('1')
    elif opc == 2:
        print('2')
    elif opc == 3:
        print('3')
    elif opc == 4:
        print('4')
    elif opc == 5:
        r = str(input("Deseja continuar [S/N]: "))
    else:
        print('Opção invalida')

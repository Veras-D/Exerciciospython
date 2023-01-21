n = int(input('Digite um numero inteiro? '))
print('''1 - Binario
2 - Octal
3 - Hexadecimal''')
o = int(input('Escolha uma opção: '))
if o == 1:
    print('Binario')
    b = str(bin(n).replace('b', ''))
    print(b[1:])
elif o == 2:
    print('Octal')
    octal = str(oct(n)).replace('o', '')
    print(octal[1:])
elif o == 3:
    print('Hexadecimal')
    x = str(hex(n)).replace('x', '')
    print(x[1:])
else:
    print('Essa opção não é valida.')

nome = str(input('Qual seu nome? '))
print(f'Bom dia, {nome}, que nome lindo você tem!'if nome == 'Danilo Veras' else f'Bom dia, {nome}!')

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
n3 = float(input('Digite a 3° nota: '))
f = float(input('Digite quantidade de faltas: '))
m = (n1 + n2 + n3) / 3
if m >= 7 and f <= 25:
    print('Aprovado')
elif 5 >= m >= 7 and f <= 25:
    final = float(input('Qual a nota da final? '))
    if final >= 5:
        print('Aprovado por final')
    else:
        print('Reprovado em final')
elif m < 5:
    print('Reprovado por nota')
elif f > 25:
    print('Reprovado por falta')

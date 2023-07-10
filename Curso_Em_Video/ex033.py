# método 1
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
lista = [n1, n2, n3]
OrdList = sorted(lista)
print(f'O menor numero é {OrdList[0]} e o maior numero é {OrdList[2]}.')
# método 2
if n1 / n3 >= 1 and n2 / n3 >=1:
    if n1 / n2 >= 1:
        print(f'O menor numero é {n3} e o maior numero é {n1}.')
    elif n2 / n1 >=1:
        print(f'O menor numero é {n3} e o maior numero é {n2}.')
elif n1 / n2 >= 1 and n3 / n2 >=1:
    if n1 / n3 >= 1:
        print(f'O menor numero é {n2} e o maior numero é {n1}.')
    elif n3 / n1 >=1:
        print(f'O menor numero é {n2} e o maior numero é {n3}.')
elif n2 / n1 >= 1 and n3 / n1 >= 1:
    if n2 / n3 >= 1:
        print(f'O menor numero é {n1} e o maior numero é {n2}.')
    elif n3 / n2 >= 1:
        print(f'O menor numero é {n1} e o maior numero é {n3}.')

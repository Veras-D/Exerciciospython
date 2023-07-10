# Escolher um de 4 alunos
import random
n1 = str(input('digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 3° aluno: '))
n4 = str(input('Digite o nome dp 4° aluno: '))
lista = [n1, n2, n3, n4]
Sorteado = random.choice(lista)
print(f'O aluno {Sorteado} irá apagar o quadro.')

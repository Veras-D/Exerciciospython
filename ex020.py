# O mesmo professor do desafio 019 quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
import random
n1 = input('Digite o nome do 1° aluno: ')
n2 = input('Digite o nome do 2° aluno: ')
n3 = input('Digite o nome do 3° aluno: ')
n4 = input('Digite o nome do 4° aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem será:\n{lista}')

# Faça um algoritmo que leia o salário de
# um funcionário e mostre seu novo salário,
# com 15% de aumento.
NOME = input('Digite o nome do funcionário que deve receber o aumento de 15%: ')
S = float(input('Digite o salario do funcionário: '))
NS = S*1.15
print(f'O novo salario do funcionário {NOME} sera: {NS:.2f} R$')

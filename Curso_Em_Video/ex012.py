# Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% (ou mais)
# de desconto.
d = float(input(f'Digite um desconto em %:'))
v = float(input('digite o valor da venda: R$ '))
vf = v*(1-(d/100))
print(f'O valor final é: {vf:.2f} R$')

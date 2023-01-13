d = float(input('Qual a distancia da viagem? '))
p = d * 0.5
if d <= 200:
    print(f'O preço da viagem é de {p:.2f} reais.')
elif d > 200:
    pd = (d - 200) * 0.45 + 100
    print(f'''Parabens você ganhou um desconto o preço da passagem é de {p:.2f} reais, mas com o desconto fica {pd:.2f} 
reais.''')
# p = d * 0.5 if d <= 200 else (d - 200) * 0.45 + 100

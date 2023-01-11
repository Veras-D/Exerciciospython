v = float(input('Qual a velocidade do carro (km/h)? '))
if v > 80:
    m = (v - 80)*7
    print(f'Você está acima da velocidade permitida de 80 km/h, portanto devera pagar uma multa de {m:.2f} reais.')
else:
    print('Dirija com atenção.')
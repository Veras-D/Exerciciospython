d = int(input('Quantos dias o veiculo foi alugado? '))
k = float(input('Quantos quilômetros foram rodados no veiculo? '))
A = (d * 60) + (k * 0.15)
print(f'O aluguel do carro é {A:.2f} R$')

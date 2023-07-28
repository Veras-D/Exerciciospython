# Aula while
c = 1
r = 's'
par = 0
impar = 0
while r == 's':  # Flag, condição de parada
    c = int(input('Digite um valor: '))
    if c % 2 == 0:
        par += 1
    else:
        impar += 1
    r = str(input('Deseja continuar [S/N]: ')).lower()
print(f'Pares: {par}\nImpares: {impar}')

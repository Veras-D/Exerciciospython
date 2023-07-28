import random
cont = 1
comp = random.randint(1, 10)
print('ADIVINHE O NUMERO ENTRE 1 E 10')
user = int(input('Digite seu resposta: '))
while user != comp:
    cont += 1
    user = int(input('Você errou, tente novamente: '))
print(f'Parabens você acertou em {cont} tentativas.')

from random import choice
from time import sleep as esperar
nums = [0, 1, 2, 3, 4, 5]
NumC = choice(nums)
print('===' * 8)
print('VAmos jogar um jogo!!!')
print('===' * 8)
NumP = int(input('Tente adivinhar um numero de 0 a 5: '))
print('PROCESSANDO...')
esperar(3)
if NumP == NumC:
    print('Parabens, você acertou o numero escolhido pelo computador!!!')
else:
    print(f'Que pena, você errou, o numero escolhido pelo computador foi {NumC}.')
# randint pode fazer o mesmo que o choice sem a lista ex: randint(0, 5)

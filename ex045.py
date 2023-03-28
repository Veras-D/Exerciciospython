import random
import time
print('''[1] - Pedra 
[2] - Papel
[3] - Tesoura''')
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Qual sua jogada? '))
comp = random.randint(1, 3)
if jogador < 4:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    if jogador == comp:
        print(f'Você e o computador escolheram {escolhas[jogador - 1]}, portanto o resultado é EMPATE!!!')
    elif jogador == 1 and comp == 3:
        print(f'''O jogador escolheu {escolhas[jogador - 1]} e o computador escolheu {escolhas[comp - 1]}, portanto o 
resultado é VITORIA!!!''')
    elif jogador == 2 and comp == 1:
        print(f'''O jogador escolheu {escolhas[jogador - 1]} e o computador escolheu {escolhas[comp - 1]}, portanto o 
resultado é VITORIA!!!''')
    elif jogador == 3 and comp == 2:
        print(f'''O jogador escolheu {escolhas[jogador - 1]} e o computador escolheu {escolhas[comp - 1]}, portanto o 
resultado é VITORIA!!!''')
    else:
        print(f'''O jogador escolheu {escolhas[jogador - 1]} e o computador escolheu {escolhas[comp - 1]}, portanto o 
resultado é DERROTA!!!''')
else:
    print('Opção invalida.')

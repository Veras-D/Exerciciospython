"""
Par ou impar Game
Date: 24/01/26
Author: Veras-D
"""
import random

cont = 0
estados = ["P", "I"]
while True:
    player_num = int(input("Escolha um numero: "))
    estado = ""
    while estado not in estados:
        estado = str(input("Par ou Impar [P/I]: ")).upper().strip()[0]
    comp_num = random.randint(0, 10)
    print(f"O computador escolheu: {comp_num}")
    if (player_num + comp_num) % 2 == 0:
        resultado = estados[0]
    else:
        resultado = estados[1]
    if resultado == estado:
        cont += 1
        print("Você ganhou")
    else:
        print("Você perdeu")
        break
print(f"Você ganhou {cont} vezes" if cont != 1 else f"Você ganhou {cont} vez")

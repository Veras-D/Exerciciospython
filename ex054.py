"""
Classificar pessoas pela idade
Author: Veras-D
Date: 02/04/23
"""
from datetime import date
de_menor = 0
de_maior = 0
pessoas = 0
n_identificados = 0
while pessoas <= 0:
    pessoas = int(input('Quantas pessoas deseja classificar? '))
for cont in range(1, pessoas + 1):
    ano_n = int(input(f'Em que ano nasceu a {cont}° pessoa? '))
    idade = date.today().year - ano_n
    if 0 <= idade < 18:
        de_menor += 1
    elif 18 <= idade <= 120:
        de_maior += 1
    else:
        n_identificados += 1
pessoa = 'pessoa' if pessoas == 1 else 'pessoas'
menor = 'é menor de idade' if de_menor == 1 else 'são menores de idade'
maior = 'é maior de idade' if de_maior == 1 else 'são maiores de idade'
classificado = 'foi capaz de ser identificado' if n_identificados == 1 else 'foram capazes de serem identificados'
print(f'De {pessoas} {pessoa} {de_menor} {menor}, {de_maior} {maior} e {n_identificados} não {classificado}.')

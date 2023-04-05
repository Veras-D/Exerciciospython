pesos = []
pesos_2 = []
for cont in range(0, 5):
    peso = float(input(f'Qual o peso da {cont + 1}° pessoa? '))
    pesos_2.append(peso)
    pesos.append(peso)
pesos.sort()
print(f'A {pesos_2.index(pesos[4]) + 1}° é a pessoa mais pesada pesando {pesos[4]} kg e a {pesos_2.index(pesos[0]) + 1} pessoa é a mais leve pesando {pesos[0]} kg.')

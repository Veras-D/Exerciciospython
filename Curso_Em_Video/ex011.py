# Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de
# tinta pinta uma área de 2 metros quadrados.
L = float(input('Digite a largura da parede em metros: '))
A = float(input('Digite a altura da parede em metros: '))
AREA = L*A
BT = AREA/2
print(f'A area da parede é {AREA:.3f} metros quadrados e são necessários {BT:.3f} baldes de tinta para pintala.')

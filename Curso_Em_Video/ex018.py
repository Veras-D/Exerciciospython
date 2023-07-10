import math
print('Descubra seno, cosseno e tangente de um ângulo!')
alfa = float(input('Escreva um ângulo em graus: '))
Rad = alfa * math.pi / 180
Sin = math.sin(Rad)
Cos = math.cos(Rad)
Tan = math.tan(Rad)
print(f'Para o ângulo de {alfa}°\nO seno é {Sin:.2f}\nO cosseno é {Cos:.2f}\nE a tangente é {Tan:.2f}!')
# math.radians() transforma de angulo para radiano

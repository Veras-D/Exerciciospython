import math
print('Descubra o terceiro lado de um triangulo qualquer!')
A = float(input('Digite um valor para o 1° lado: '))
B = float(input('Digite um valor para o 2° lado: '))
alfa = int(input('Digite o ângulo entre os lados em graus(°): '))
Rad = alfa * math.pi / 180
C_quadr = pow(A, 2) + pow(B, 2) - (2 * A * B * math.cos(Rad))
C = math.sqrt(C_quadr)
print(f'O triangulo de lados {A:.2f} e {B:.2f} com ângulo de {alfa}° tem terceiro lado igual a {C:.2f}!')
# math.hypot() calcula a hipotenusa de um triangulo retângulo

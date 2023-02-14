from math import *
import numpy as np

# numero de elos
num_elo = int(input('Qual o numero de elo? '))
if num_elo == 1:
    # 2 elos
    # Variáveis iniciais
    L = float(input('Qual o comprimento da barra? '))
    massa_2 = float(input('Qual a massa da barra? '))
    theta_2 = radians(float(input('Qual o angulo da barra? ')))
    mod_Fp = float(input('Qual o modulo de Fp? '))
    ang_Fp = radians(float(input('Qual o ângulo de Fp? ')))
    aG_mod = float(input('Qual o modulo da aceleração? '))
    aG_ang = radians(float(input('Qual o angulo da aceleração? ')))
    omega_2 = float(input('Qual velocidade angular da barra'))
    alfa_2 = float(input('Qual aceleração angular da barra'))
    mon_inercia = float(input('Qual o momento de inercia da barra'))
    # vetores e pontos
    CG = np.array([L * 0.5 * cos(theta_2), L * 0.5 * sin(theta_2)])
    Px = float(input('Qual a coordenada x de P? '))
    Py = float(input('Qual a coordenada y de P? '))
    P = np.array([Px, Py])
    R12 = np.multiply(-1, CG)
    Rp = P - CG
    Fp = np.array([mod_Fp * cos(ang_Fp), mod_Fp * sin(ang_Fp)])
    aG = np.array([aG_mod * cos(aG_ang), aG_mod * sin(aG_ang)])
    # Matrizes
    A = np.array([[1, 0, 1], [0, 1, 0], [-R12[0], R12[1], 1]])
    RpXFp = Rp[0] * Fp[1] - Rp[1] * Fp[0]
    C = np.array([[massa_2 * aG[0] - Fp[0]], [massa_2 * aG[1] - Fp[1]], [mon_inercia * alfa_2 - RpXFp]])
    B = np.linalg.solve(A, C)
    # Resultados
    F12_mod = sqrt(pow(B[0], 2) + pow(B[1], 2))
    F12_ang = degrees(atan(B[1] / B[0]))
    T12 = B[2]
    print(f'O modulo de F12 é {F12_mod:.4f}, na direção {F12_ang:.f} e o valor de T12 é {T12:.4f}.')
elif num_elo == 3:
# 3 elos
# Variáveis iniciais
    L2 = float(input('Qual o comprimento da barra 2? '))
    massa_2 = float(input('Qual o massa da barra 2? '))
    theta_2 = radians(float(input('Qual o angulo da barra 2? ')))
    aG2_mod = float(input('Qual o modulo da aceleração 2? '))
    aG2_ang = radians(float(input('Qual o angulo da aceleração 2? ')))
    omega_2 = float(input('Qual velocidade angular da barra 2'))
    alfa_2 = float(input('Qual aceleração angular da barra 2'))
    mon_inercia_2 = float(input('Qual o momento de inercia da barra 2'))
    L3 = float(input('Qual o comprimento da barra 3? '))
    massa_3 = float(input('Qual o massa da barra 3? '))
    theta_3 = radians(float(input('Qual o angulo da barra 3? ')))
    aG3_mod = float(input('Qual o modulo da aceleração 3? '))
    aG3_ang = radians(float(input('Qual o angulo da aceleração 3? ')))
    omega_3 = float(input('Qual velocidade angular da barra 3'))
    alfa_3 = float(input('Qual aceleração angular da barra 3'))
    mon_inercia_3 = float(input('Qual o momento de inercia da barra 3'))
    mod_Fp = float(input('Qual o modulo de Fp? '))
    ang_Fp = radians(float(input('Qual o ângulo de Fp? ')))
# vetores e pontos
    # verificar valores do centro de gravidade
    # O exercício da a distancia e o angulo do CG
    CG2 = np.array([L2 * 0.5 * cos(theta_2), L2 * 0.5 * sin(theta_2)])
    CG3 = np.array([L3 * 0.5 * cos(theta_3), L3 * 0.5 * sin(theta_3)])
    # verificar valores do centro de gravidade
    Px = float(input('Qual a coordenada x de P? '))
    Py = float(input('Qual a coordenada y de P? '))
    P = np.array([Px, Py])
    Rp = P - CG3
# Matrizes
# Resultados
elif num_elo == 4:
# 4 elos
# Variáveis iniciais

# vetores e pontos
# Matrizes
# Resultados
else:
    print('Opção invalida')

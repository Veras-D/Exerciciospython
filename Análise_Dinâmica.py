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
    theta_2_R12 = radians(180) + theta_2
    mod_Fp = float(input('Qual o modulo de Fp? '))
    ang_Fp = radians(float(input('Qual o ângulo de Fp? ')))
    aG_mod = float(input('Qual o modulo da aceleração? '))
    aG_ang = radians(float(input('Qual o angulo da aceleração? ')))
    omega_2 = float(input('Qual velocidade angular da barra? '))
    alfa_2 = float(input('Qual aceleração angular da barra? '))
    mon_inercia = float(input('Qual o momento de inercia da barra? '))
    # vetores e pontos
    CG = np.array([L * 0.5 * cos(theta_2), L * 0.5 * sin(theta_2)])
#    Px = float(input('Qual a coordenada x de P? '))
#    Py = float(input('Qual a coordenada y de P? '))
    P = np.array([L * cos(theta_2), L * sin(theta_2)])
    R12 = np.array([L * 0.5 * cos(theta_2_R12), L * 0.5 * sin(theta_2_R12)])
    Rp = P - CG
    Fp = np.array([mod_Fp * cos(ang_Fp), mod_Fp * sin(ang_Fp)])
    aG = np.array([aG_mod * cos(aG_ang), aG_mod * sin(aG_ang)])
    # Matrizes
    A = np.array([[1, 0, 1], [0, 1, 0], [-R12[1], R12[0], 1]])
    RpXFp = Rp[0] * Fp[1] - Rp[1] * Fp[0]
    C = np.array([[massa_2 * aG[0] - Fp[0]], [massa_2 * aG[1] - Fp[1]], [mon_inercia * alfa_2 - RpXFp]])
    B = np.linalg.solve(A, C)
    # Resultados
    F12_mod = hypot(B[0], B[1])
    F12_ang = degrees(atan2(B[1], B[0]))
    T12 = B[2]
    print(B)
    print(F12_mod)
    print(F12_ang)
#    print(f'O modulo de F12 é {F12_mod:.4f}, na direção {F12_ang:.4f} e o valor de T12 é {T12:.4f}.')
elif num_elo == 3:
# 3 elos
# Variáveis iniciais
    L2 = float(input('Qual o comprimento da barra 2  (em metros)? '))
    massa_2 = float(input('Qual o massa da barra 2? '))
    theta_2 = radians(float(input('Qual o angulo da barra 2? ')))
    aG2_mod = float(input('Qual o modulo da aceleração 2? '))
    aG2_ang = radians(float(input('Qual o angulo da aceleração 2? ')))
    omega_2 = float(input('Qual velocidade angular da barra 2? '))
    alfa_2 = float(input('Qual aceleração angular da barra 2? '))
    mon_inercia_2 = float(input('Qual o momento de inercia da barra 2? '))
    CG2_d = float(input('Qual a distancia do CG2 até a barra 2? '))
    CG2_a = radians(float(input('Qual ângulo entre o CG2 e a barra 2? '))) + theta_2
    L3 = float(input('Qual o comprimento da barra 3? '))
    massa_3 = float(input('Qual o massa da barra 3? '))
    theta_3 = radians(float(input('Qual o angulo da barra 3? ')))
    aG3_mod = float(input('Qual o modulo da aceleração 3? '))
    aG3_ang = radians(float(input('Qual o angulo da aceleração 3? ')))
    omega_3 = float(input('Qual velocidade angular da barra 3? '))
    alfa_3 = float(input('Qual aceleração angular da barra 3? '))
    mon_inercia_3 = float(input('Qual o momento de inercia da barra 3? '))
    CG3_d = float(input('Qual a distancia do CG3 até a barra 3? '))
    CG3_a = radians(float(input('Qual ângulo entre o CG3 e a barra 3? '))) + theta_3
    mod_Fp = float(input('Qual o modulo de Fp? '))
    ang_Fp = radians(float(input('Qual o ângulo de Fp? ')))
    lanb = float(input('Qual o coeficiente de atrito? '))
# vetores e pontos
    # verificar valores do centro de gravidade
    # O exercício da a distancia e o angulo do CG
    CG2 = np.array([CG2_d * cos(CG2_a), CG2_d * sin(CG2_a)])
    CG3 = np.array([CG3_d * cos(CG3_a), CG3_d * sin(CG3_a)])
    # verificar valores do centro de gravidade
    mod_P = float(input('Qual a distancia do CG3 até o ponto P? '))
    ang_P = radians(float(input('Qual o ângulo entre o CG3 e o elo 3? ')))
    Px = mod_P * cos(ang_P)
    Py = mod_P * sin(ang_P)
    Rp = np.array([Px, Py])
    R12 = [0, 0] - CG2
    R32 = [L2 * cos(theta_2), L2 * sin(theta_2)] - CG2
    R23 = [L2 * cos(theta_2), L2 * sin(theta_2)] - CG3
    R13 = [L3 * cos(theta_3), L3 * sin(theta_3)] - CG3
    Fp = np.array([mod_Fp * cos(ang_Fp), mod_Fp * sin(ang_Fp)])
    aG2 = np.array([aG2_mod * cos(aG2_ang), aG2_mod * sin(aG2_ang)])
    aG3 = np.array([aG3_mod * cos(aG3_ang), aG3_mod * sin(aG3_ang)])
# Matrizes
    lanbXR13 = lanb * R13[0] - R13[1]
    A = np.array([[1, 0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0],
                  [-R12[1], R12[0], -R32[1], R32[0], 0, 1],
                  [0, 0, -1, 0, 1, 0],
                  [0, 0, 0, -1, lanb, 0],
                  [0, 0, R23[1], -R23[0], lanbXR13, 0]])
    C = np.array([[massa_2 * aG2[0]],
                  [massa_2 * aG2[1]],
                  [mon_inercia_2 * alfa_2],
                  [massa_3 * aG3[0] - Fp[0]],
                  [massa_3 * aG3[1] - Fp[1]],
                  [mon_inercia_3 * alfa_3 - Rp[0] * Fp[1] + Rp[1] * Fp[0]]])
# Resultados
    B = np.linalg.solve(A, C)
    print('''
    F12x
    F12y
    F32x
    F32y
    F13x
    T12''')
    print(B)
#elif num_elo == 4:
# 4 elos
# Variáveis iniciais

# vetores e pontos
# Matrizes
# Resultados
else:
    print('Opção invalida')

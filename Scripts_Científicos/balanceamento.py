from math import *
import numpy as np

tipo = int(input('Qual o tipo de elo? '))
if tipo == 1:
    # Tipo V - estático
    m1 = float(input('Qual a massa 1? '))
    m2 = float(input('Qual a massa 2? '))
    # Raio é a distância do centro até o CG
    r1_d = float(input('Qual o raio 1? '))
    r2_d = float(input('Qual o raio 2? '))
    theta_2 = float(input('Qual o ângulo entre o eixo x e o raio 1? '))
    theta_3 = float(input('Qual o ângulo entre o eixo x e o raio 2? '))
    r1 = np.array([r1_d * cos(theta_2), r1_d * sin(theta_2)])
    r2 = np.array([r2_d * cos(theta_3), r2_d * sin(theta_3)])
    rG_ang = degrees(atan2(m1 * r1[1] + m2 * r2[1], m1 * r1[0] + m2 * r2[0]))
    rG_mod = hypot(m1 * r1[0] + m2 * r2[0], m1 * r1[1] + m2 * r2[1])
    print(rG_mod, rG_ang)
if tipo == 2:
    # Tipo ventilador de 3 pontas - estático
    m1 = float(input('Qual a massa 1? '))
    m2 = float(input('Qual a massa 2? '))
    m3 = float(input('Qual a massa 3? '))
    r1_d = float(input('Qual o raio 1? '))
    r2_d = float(input('Qual o raio 2? '))
    r3_d = float(input('Qual o raio 3? '))
    theta_2 = float(input('Qual o ângulo entre o eixo x e o raio 1? '))
    theta_3 = float(input('Qual o ângulo entre o eixo x e o raio 2? '))
    theta_4 = float(input('Qual o ângulo entre o eixo x e o raio 3? '))
    r1 = np.array([r1_d * cos(theta_2), r1_d * sin(theta_2)])
    r2 = np.array([r2_d * cos(theta_3), r2_d * sin(theta_3)])
    r3 = np.array([r3_d * cos(theta_4), r3_d * sin(theta_4)])
    rG_ang = degrees(atan2(m1 * r1[1] + m2 * r2[1] + m3 * r3[1], m1 * r1[0] + m2 * r2[0] + m3 * r3[0]))
    rG_mod = hypot(m1 * r1[0] + m2 * r2[0] + m3 * r3[0], m1 * r1[1] + m2 * r2[1] + m3 * r3[1])
    print(rG_mod, rG_ang)

# ex 12-4
if tipo == 3:
    p = 8.9
    v = 0.05
    theta_2 = radians(0)
    theta_3 = radians(120)
    theta_4 = radians(240)
    m1 = (1 + v) * p / 9.81
    m2 = (1 - v) * p / 9.81
    m3 = (1 - v) * p / 9.81
    alt = 0.03175
    r1 = np.array([alt * cos(theta_2), alt * sin(theta_2)])
    r2 = np.array([alt * cos(theta_3), alt * sin(theta_3)])
    r3 = np.array([alt * cos(theta_4), alt * sin(theta_4)])
    mRbx = -1 * (m1 * r1[0] + m2 * r2[0] + m3 * r3[0])
    mRby = -1 * (m1 * r1[1] + m2 * r2[1] + m3 * r3[1])
    rG_ang = degrees(atan2(mRby, mRbx))
    rG_mod = hypot(mRbx, mRby)
    print(rG_mod, rG_ang)
    dis_sup = 1.2192
    var_CG = 0.1
    re = dis_sup * var_CG
    mRbe = (m1 + m2 + m3) * re
    print(mRbe)
    Rcw = 0.0508
    mRb = rG_mod + mRbe
    print(mRb)
    mcw = mRb / Rcw
    print(mcw)

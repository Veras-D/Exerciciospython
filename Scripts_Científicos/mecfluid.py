from math import *
import CoolProp
import pyromat as pm
"""
P_A = 172.73 * 10**3  # Pa
ρ_água = 998.9  # kg * m^-3
g = 9.8  # m * s^-2
γ_SAE30 = 8720  # N * m^-3
SG = 1.45
P_B = -ρ_água * g * 4*10**(-2) + γ_SAE30 * (3 + 6 - 3)*10**(-2) - ρ_água * SG * g * (5 + 8 - 3)*10**(-2) + P_A
print(P_B)  # Pa
"""
"""
p = 1.94
g = 32.2
L = 9.85
w = 6.75
theta = radians(30)
P = (2/3) * p * g * tan(theta) * w * L ** 2  # lbf
print(P)
"""
"""
a = 1  # m^-2
p = 998.9  # kg * m^-3
g = 9.8  # m * s^-2
D = 1.2  # m
L = 1.5  # m
H = 1.4  # m
F_vert = a * p * g * L * (D**4) / 4  # N
xcp_X_F_vert = a ** 2 * p * g * L * (D**7) / 14  # N*m
ycp_X_F_horizontal = p * g * L * (D ** 3) / 6  # N*m
Fa = (xcp_X_F_vert + ycp_X_F_horizontal) / H  # N
print(f'Força vertical: {F_vert} N'
      f'\nMomento da força vertical: {xcp_X_F_vert} N.m'
      f'\nMomento da força horizontal: {ycp_X_F_horizontal} N.m'
      f'\nForça aplicada no ponto A: {Fa} N')
"""
"""
p = 998.9  # kg * m^-3
g = 9.8  # m * s^-2
d = 0.025 * 10**-3  # m
Vol = pi * (d ** 3) / 6  # m^3
Fe = p * g * Vol  # N
mi = 1 * 10 ** -3  # N*s*m^-2
P = 1.1 * 101000  # N*m^-2
R = 4124  # J*K*kg^-1
T = 20 + 273.15  # K
m = (P * Vol) / (R * T)
Peso = m * g
V = (Fe - Peso) / (3 * pi * mi * d)  # m*s^-1
print(f'Força de empuxo: {Fe} N\n'
      f'Velocidade terminal: {V} m/s')
"""

import pandas as pd
import numpy as np
i = 4 / 2  # tempos
z = 4
n = 2800 / 60  # rps
cv = 0.717  # kJ / kg * k
cp = 1.0048  # kJ / kg * k
R = cp - cv  # kJ / kg * k
r = 10
k = 1.4
# 1
P1 = 101.3  # kpa
T1 = 300  # K
V1 = 0.00006  # m³
m = (P1 * V1) / (R * T1)
# 2
P2 = P1 * r ** k
T2 = T1 * r ** (k - 1)
V2 = V1 / r
# 3
P3 = 7500  # kpa
T3 = P3 * T2 / P2
V3 = V2
# 4
P4 = P3 / r**k
T4 = T3 / r ** (k - 1)
V4 = V1
# final
qh = abs(cv * (T3 - T2))
ql = abs(cv * (T4 - T1))
wliq = qh - ql
N_c = m * wliq * n * z / i
print(N_c)
PME = wliq * m / (V1 - V2)
n_t = 1 - 1 / (r ** (k - 1))


R1 = P1 * V1 / (m * T1)
R2 = P2 * V2 / (m * T2)
R3 = P3 * V3 / (m * T3)
R4 = P4 * V4 / (m * T4)

estados = np.array([[P1, T1, V1, R1],
                    [P2, T2, V2, R2],
                    [P3, T3, V3, R3],
                    [P4, T4, V4, R4],])
df = pd.DataFrame(estados)
df.columns = ["Pressão (kpa)", "Temperatura (k)", "Vol. Especifico (m^3 / kg)", "R (kJ / kg * k)"]
df.index = range(1, len(df) + 1)
print(df)
print(f'Potencia do ciclo em hp: {N_c * (1 / 0.7458)}')
print(f'PME: {PME}')
print(f'Rendimento: {n_t * 100}')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from math import *
P1 = 100  # kpa
T1 = 27 + 273.15  # k
# T5 ou q_sai = ???
r = 18  # ou 8???
rc = 1.2
rp = 1.5
cv = 0.717  # kJ / kg * k
cp = 1.0048  # kJ / kg * k
R = cp - cv  # kJ / kg * k
v1 = (R * T1) / P1
v5 = v1
# P * v = R * T
k = cp / cv
# P1 * v1 ** k = P2 * v2 ** k
# 1-2
P2 = P1 * r ** k
T2 = T1 * r ** (k - 1)
v2 = v1 / r
# 2-3
P3 = P2 * rp
T3 = T2 * rp
v3 = v2
q23 = cv * (T3 - T2)
# 3-4
P4 = P3
T4 = T3 * rc
v4 = v3 * rc
# 4-5
P5 = P4 * (rc / r) ** k
T5 = T4 * (rc / r) ** (k - 1)
# 5-1

# final
w12 = cv * (T2 - T1)
w34 = P3 * (v4 - v3)
w45 = cv * (T5 - T4)
q34 = cp * (T4 - T3)
q_ent = abs(q23) + abs(q34)
q_sai = abs(cv * (T5 - T1))
w_liq1 = q_ent - q_sai
w_liq2 = w34 - 1 * (w45 + w12)
nt1 = 1 - (1 / r ** (k - 1)) * ((rp * (rc ** k) - 1) / ((rp - 1) + k * rp * (rc - 1)))
nt2 = 1 - q_sai / q_ent
pme = w_liq1 / (v1 - v2)
print(nt1, nt2)
R1 = P1 * v1 / T1
R2 = P2 * v2 / T2
R3 = P3 * v3 / T3
R4 = P4 * v4 / T4
R5 = P5 * v5 / T5
estados = np.array([[P1, T1, v1, R1],
                    [P2, T2, v2, R2],
                    [P3, T3, v3, R3],
                    [P4, T4, v4, R4],
                    [P5, T5, v5, R5]])
df = pd.DataFrame(estados)
df.columns = ["Pressão (kpa)", "Temperatura (k)", "Vol. Especifico (m^3 / kg)", "R (kJ / kg * k)"]
df.index = range(1, len(df) + 1)
print(df)
# fazer gráficos P-v e T-s
P = np.array([P1, P2, P3, P4, P5, P1])
v = np.array([v1, v2, v3, v4, v5, v1])
plt.plot(v, P)
plt.show()
# tentar fazer um grafico melhor

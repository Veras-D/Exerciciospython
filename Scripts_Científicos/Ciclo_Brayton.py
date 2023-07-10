import pandas as pd
import numpy as np
select = int(input('[1] - Ciclo simples\n[2] - Ciclo com regenerador ideal\n[3] - Ciclo com Inter-Resfriamento\n\n'
                   'Escolha Uma Opção: '))
irrev = int(input('O ciclo é irreversível?\n[0] - NÃO\n[1] - SIM\nEscolha uma opção: '))
# P * v = R * T
cv = 0.717  # kJ / kg * k
cp = 1.0048  # kJ / kg * k
R = cp - cv  # kJ / kg * k
k = cp / cv
rp = 22  # razão de pressão P2 / P1

# Ar Atmosférico
P1 = 100  # kpa
T1 = 300  # k
v1 = (R * T1) / P1  # m³/kg

# trazer ponto 2 para fora também
P2 = rp * P1  # kpa
T2 = T1 * rp ** ((k - 1) / k)  # k
v2 = R * T2 / P1  # m³/kg

if select == 1 and irrev == 0:
    # Ciclo simples ideal
    print('Ciclo simples ideal')
    T3 = 1700  # k
    P3 = P2  # kpa
    P4 = P1  # kpa
    T4 = T3 * (P4 / P3) ** ((k - 1) / k)  # k
    v3 = R * T3 / P3  # m³/kg
    v4 = R * T4 / P4  # m³/kg

    R1 = P1 * v1 / T1
    R2 = P2 * v2 / T2
    R3 = P3 * v3 / T3
    R4 = P4 * v4 / T4

    w_comp_esp = cp * (T2 - T1)  # kj/kg
    q_quei_esp = cp * (T3 - T2)  # kj/kg
    w_turb_esp = cp * (T3 - T4)  # kj/kg
    w_liq_esp = w_turb_esp - w_comp_esp  # kj/kg
    Rend_Real = w_liq_esp / q_quei_esp
    Rend_Teorico = 1 - 1 / (rp ** ((k - 1) / k))

    estados = np.array([[P1, T1, v1, R1],
                        [P2, T2, v2, R2],
                        [P3, T3, v3, R3],
                        [P4, T4, v4, R4]])
    df = pd.DataFrame(estados)
    df.columns = ["Pressão (kpa)", "Temperatura (k)", "Vol. Especifico (m^3 / kg)", "R (kJ / kg * k)"]
    df.index = range(1, len(df) + 1)
    print(df)

    print(f'Trabalho especifico do compressor: {w_comp_esp:.2f} kj/kg'
          f'\nTrabalho especifico da turbina: {w_turb_esp:.2f} kj/kg'
          f'\nTrabalho liquido especifico: {w_liq_esp:.2f} kj/kg'
          f'\nQuantidade de calor do queimador especifico: {q_quei_esp:.2f} kj/kg'
          f'\nRendimento Real: {Rend_Real:.2f}%'
          f'\nRendimento Teórico: {Rend_Teorico:.2f}%')
elif select == 1 and irrev == 1:
    # Ciclo simples com irreversibilidade [POR ULTIMO]
    print('Ciclo simples com irreversibilidade')
elif select == 2 and irrev == 0:
    # Ciclo com regenerador
    print('Ciclo com regenerador')
elif select == 2 and irrev == 1:
    # Ciclo com regenerador irreversível [POR ULTIMO]
    print('Ciclo com regenerador irreversível')
elif select == 3 and irrev == 0:
    # Ciclo com Inter-Resfriamento ideal
    print('Ciclo com Inter-Resfriamento ideal')
elif select == 3 and irrev == 1:
    # Ciclo com Inter-Resfriamento irreversível [POR ULTIMO]
    print('Ciclo com Inter-Resfriamento irreversível')
else:
    print('Opção Invalida')

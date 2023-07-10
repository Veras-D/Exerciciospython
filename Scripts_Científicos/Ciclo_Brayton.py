import pandas as pd
import numpy as np
teste = [1, 2, 3, 4, 5]
select = int(input('[1] - Ciclo simples\n[2] - Ciclo com regenerador ideal\n[3] - Ciclo com Inter-Resfriamento\n\n'
                   'Escolha Uma Opção: '))
irrev = int(input('\nO ciclo é irreversível?\n[0] - NÃO\n[1] - SIM\nEscolha uma opção: '))
# P * v = R * T
cv = 0.717  # kJ / kg * k
cp = 1.0048  # kJ / kg * k
R = cp - cv  # kJ / kg * k
k = cp / cv
rp = 15  # razão de pressão P2 / P1

# Ar Atmosférico
P1 = 100  # kpa
T1 = 300  # k
v1 = (R * T1) / P1  # m³/kg

# trazer ponto 2 para fora também
P2 = rp * P1  # kpa
T2 = T1 * (P2 / P1) ** ((k - 1) / k)  # k
v2 = R * T2 / P1  # m³/kg

if select == 1 and irrev == 0:
    # Ciclo simples ideal
    print('\nCiclo simples ideal')
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
    bwr = w_comp_esp / w_turb_esp

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
          f'\nRendimento Calculado: {100 * Rend_Real:.2f}%'
          f'\nRendimento Teórico: {100 * Rend_Teorico:.2f}%'
          f'\nbwr = {100 * bwr:.2f}%')

elif select == 1 and irrev == 1:
    # Ciclo simples com irreversibilidade [POR ULTIMO]
    print('\nCiclo simples com irreversibilidade')

elif select == 2 and irrev == 0:
    # Ciclo com regenerador
    print('\nCiclo com regenerador')
    T4 = 1400  # k
    P3 = P2
    P4 = P2
    P5 = P1
    T5 = T4 * (P5 / P4) ** ((k - 1) / k)  # k
    P6 = P1
    E = 0.8  # efetividade_do_regenerador
    T3 = E * (T5 - T2) + T2  # k
    T6 = T2 + T5 - T3  # k
    v3 = R * T3 / P3
    v4 = R * T4 / P4
    v5 = R * T5 / P5
    v6 = R * T6 / P6

    q_quei_esp = cp * (T4 - T3)
    q_troc_esp = cp * (T1 - T6)
    q_liq_esp = q_troc_esp + q_quei_esp
    w_turb_esp = cp * (T4 - T5)
    w_comp_esp = cp * (T1 - T2)
    w_liq_esp = w_turb_esp + w_comp_esp
    Rend_real = w_liq_esp / q_quei_esp
    bwr = abs(w_comp_esp / w_turb_esp)

    R1 = P1 * v1 / T1
    R2 = P2 * v2 / T2
    R3 = P3 * v3 / T3
    R4 = P4 * v4 / T4
    R5 = P5 * v5 / T5
    R6 = P6 * v6 / T6
    estados = np.array([[P1, T1, v1, R1],
                        [P2, T2, v2, R2],
                        [P3, T3, v3, R3],
                        [P4, T4, v4, R4],
                        [P5, T5, v5, R5],
                        [P6, T6, v6, R6]])
    df = pd.DataFrame(estados)
    df.columns = ["Pressão (kpa)", "Temperatura (k)", "Vol. Especifico (m^3 / kg)", "R (kJ / kg * k)"]
    df.index = range(1, len(df) + 1)
    print(df)

    print(f'Trabalho especifico do compressor: {w_comp_esp:.2f} kj/kg'
          f'\nTrabalho especifico da turbina: {w_turb_esp:.2f} kj/kg'
          f'\nTrabalho liquido especifico: {w_liq_esp:.2f} kj/kg'
          f'\nQuantidade de calor do queimador especifico: {q_quei_esp:.2f} kj/kg'
          f'\nQuantidade de calor liberado para o meio: {q_troc_esp} kj/kg'
          f'\nQuantidade de calor liquida especifica: {q_liq_esp} kj/kg'
          f'\nRendimento Calculado: {100 * Rend_real:.2f}%'
          f'\nbwr = {100 * bwr:.2f}%')

elif select == 2 and irrev == 1:
    # Ciclo com regenerador irreversível [POR ULTIMO]
    print('\nCiclo com regenerador irreversível')
elif select == 3 and irrev == 0:
    # Ciclo com Inter-Resfriamento ideal
    print('\nCiclo com Inter-Resfriamento ideal')
elif select == 3 and irrev == 1:
    # Ciclo com Inter-Resfriamento irreversível [POR ULTIMO]
    print('\nCiclo com Inter-Resfriamento irreversível')
else:
    print('\nOpção Invalida')

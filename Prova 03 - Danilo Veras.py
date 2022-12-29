v = -1
p = -1
u = -1
D = 43
while v < 0:
    v = float(input('Insira a velocidade média do fluido: '))
    if v < 0:
        print('Digite um valor positivo')
while p <= 0:
    p = float(input('Insira a massa específica do fluido: '))
    if p < 0:
        print('Digite um valor positivo')
while u < 0:
    u = float(input('Insira a viscosidade dinâmica do fluido: '))
    if v < 0:
        print('Digite um valor positivo')
Re = (p * v * D) / u
if Re <= 2000:
    print(f'O coeficiente de Reynolds calculado foi {Re:.2f}, portanto o escoamento é laminar')
elif 2000 < Re < 2400:
    print(f'O coeficiente de Reynolds calculado foi {Re:.2f}, portanto o escoamento é de transição')
elif Re >= 2400:
    print(f'O coeficiente de Reynolds calculado foi {Re:.2f}, portanto o escoamento é turbulento')
else:
    print("Valor não definido")

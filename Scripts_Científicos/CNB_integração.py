import sympy as sp
from math import e
b = 0.6
a = 0
n = 6
h = (b - a) / n
x = sp.symbols('x')
y_vet = []
y = e ** sp.sin(x)
n_ = h
for i in range(1, n + 1):
    y_vet.append(n_**2)
    n_ += h
PeU = [y_vet[0], y_vet[-1]]
Pares = []
Impares = []
for i in range(0, n):
    if (i % 2) == 0 and i > 1:
        Pares.append(y_vet[i])
    elif (i % 2) == 1 and i < (n - 1):
        Impares.append(y_vet[i])
Met_Ret = h * sum(y_vet)
print(f'Método retangular: {Met_Ret:.2f}')
Met_Trap = 0.5 * h * (sum(PeU) + 2 * (sum(Pares) + sum(Impares)))
print(f'Método Trapezoidal: {Met_Trap:.2f}')
Met_Simp = (h / 3) * (sum(PeU) + 2 * sum(Impares) + 4 * sum(Pares))
print(f'Método de Simpson: {Met_Simp:.2f}')
Valor_exato = sp.integrate(y, (x, a, b))
print(f'Valor exato: {float(Valor_exato):.2f}')
Erro_Relativo_Ret = abs(((Valor_exato - Met_Ret) / Valor_exato) * 100)
Erro_Relativo_Trap = abs(((Valor_exato - Met_Trap) / Valor_exato) * 100)
Erro_Relativo_Simp = abs(((Valor_exato - Met_Simp) / Valor_exato) * 100)
print(f'Erro Relativo Retangular: {Erro_Relativo_Ret:.2f}%')
print(f'Erro Relativo Trapezoidal: {Erro_Relativo_Trap:.2f}%')
print(f'Erro Relativo Simpson: {Erro_Relativo_Simp:.2f}%')

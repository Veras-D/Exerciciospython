import sympy as sp
from math import e
import numpy as np
b = 2.2
a = 1
n = 10
h = (b - a) / n
x = sp.symbols('x')
y_vet = []
y = x**3 * e ** (x + 1)
n_ = h
for i in range(0, n + 1):
    y_vet.append(n_**3 * e ** (n_ + 1))
    n_ += h
PeU = [y_vet[0], y_vet[-1]]
Pares = []
Impares = []
for i in range(0, n):
    if (i % 2) == 0 and i > 1:
        Pares.append(y_vet[i])
    elif (i % 2) == 1 and i < n:
        Impares.append(y_vet[i])
Met_Simp = (h / 3) * (sum(PeU) + 4 * sum(Impares) + 2 * sum(Pares))
print(f'Método de Simpson: {Met_Simp:.4f}')
Valor_exato = sp.integrate(y, (x, a, b))
print(f'Valor exato: {float(Valor_exato):.4f}')
sp.plot(sp.diff(y, x, 4))
eq = sp.diff(y, x, 4)
valores_y = []
x_valores = np.arange(a, b, 0.01)
for i in x_valores:
    y = eq.subs({x: i})
    valores_y.append(y)
M = float(abs(np.max(valores_y)))
Erro_Simp = (M * n * h**5) / 180
print(f'Erro Simpson: {Erro_Simp}')

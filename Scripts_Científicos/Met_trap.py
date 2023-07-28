import sympy as sp
import numpy as np
b = 1
a = 0
n = 10
h = (b - a) / n
x = sp.symbols('x')
y_vet = []
y = (x**3 + 1) ** 0.5
n_ = h
for i in range(0, n + 1):
    y_vet.append((n_**3 + 1) ** 0.5)
    n_ += h
PeU = [y_vet[0], y_vet[-1]]
Met_Trap = (h / 2) * (sum(PeU) + 2 * sum(y_vet[1:-1]))
print(f'Método do Trapézio: {Met_Trap:.4f}')
Valor_exato = sp.integrate(y, (x, a, b))
print(f'Valor exato: {float(Valor_exato):.4f}')
sp.plot(sp.diff(y, x, 2), (x, a, b))
eq = sp.diff(y, x, 2)
valores_y = []
x_valores = np.arange(a, b, 0.01)
for i in x_valores:
    y = eq.subs({x: i})
    valores_y.append(y)
M = float(abs(np.max(valores_y)))
Erro_Simp = (M * (b - a)**3) / (12 * n**2)
print(f'Erro Trapézio: {Erro_Simp}')

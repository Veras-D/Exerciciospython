"""
Programa para interpolação polinomial utilizando o método de Lagrange.
O programa realiza a interpolação polinomial utilizando os pontos (xi, f(xi)) fornecidos.
Os pontos xi e f(xi) são definidos como arrays numpy.
Data: 07/03/23
Author: Veras-D
"""
import numpy as np
import sympy as sp
POL = 0
xi = np.array([6000, 6500, 7000, 7500, 8000])
f_x = np.array([13728.13, 14288.69, 14828.07, 15348.51, 15851.87])
L = []
x = sp.symbols('x')
for i in range(0, len(xi)):
    x_temp = np.delete(xi, i)
    x_subt = xi[i] - x_temp
    x_subt_x = x - x_temp
    x_mult = np.prod(x_subt)
    x_mult_x = np.prod(x_subt_x)
    Li = x_mult_x / x_mult
    print(f'L{i} = {Li}')
    L.append(Li)
    POL += f_x[i] * L[i]
POL = sp.expand(POL)
print(f'F(x)={POL}')
Resul = float(POL.subs({x: 7250}))
print(f'F(80) = {Resul}')
# sp.plot(POL, (x, 13, 17))
# eq = (sp.Eq(sp.diff(POL), 0))
# print(f'F\'(x)={eq}')
# Resul = sp.solve(eq)
# print(f'Resultado: {Resul}')

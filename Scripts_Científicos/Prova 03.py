from sympy import *
from math import pi
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
th = 50
theta = th * pi / 180
p = 1000
V = 15
A = 0.05
g = 9.81
M_expr = ((p * V**2 * A) / g) * (1 - cos(x))
M_func = lambdify(x, M_expr, modules=['numpy'])

x_vals = np.linspace(0, pi, 100)
y_vals = M_func(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel('Theta (rad)')
plt.ylabel('M (Kg)')
plt.title('Variação da massa M em função do Ângulo theta')

plt.show()

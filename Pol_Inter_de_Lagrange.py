import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
POL = 0
xi = np.array([-1, 0, 2])
f_x = np.array([4, 1, -1])
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
print(POL)

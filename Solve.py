from math import e
from scipy.optimize import fsolve
import numpy as np


def equation(x):
    return np.tan(x)*(-1) + e**x


c = 1
print(f'Chute inicial: {c}')
x0 = fsolve(equation, c)  # Chute inicial: 0
print(f'Resultado: {x0}')

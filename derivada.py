import sympy
import math
x = sympy.symbols('x')
funcao = x**2 + 2*x - math.e**(-2*x)
derivada = sympy.diff(funcao, x)
print(derivada)

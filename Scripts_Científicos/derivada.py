import sympy
import math
x = sympy.symbols('x')
pi = sympy.symbols('pi')
e = math.e
funcao = ((pi * x**3) / 6) + e**(2*x)
derivada = sympy.diff(funcao, x)
print(derivada)

from math import *
m = 45.9 * 10**-3
m_erro = 0.3 * 10**-3
d = 41.1 * 10**-3
d_erro = 0.3 * 10**-3
d_par_fun_m = 6 / (pi * d**3)
d_par_fun_d = -18 * m / (pi * d**4)
incerteza = sqrt((d_par_fun_m * m_erro)**2 + (d_par_fun_d * d_erro)**2)
print(incerteza)

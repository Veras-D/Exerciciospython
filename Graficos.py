import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 3)
y = 10*x**4-7*x**3-24*x**2-5*x+2
plt.plot(x, y)
plt.grid(True)
plt.show()

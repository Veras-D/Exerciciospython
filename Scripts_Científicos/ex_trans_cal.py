import numpy as np
from matplotlib import pyplot as plt

k = 25
x1 = np.linspace(0.01, 0.95, 10)
x2 = np.linspace(0.01, 1, 10)
y1 = np.array(100 - 150*x1 + 10*x1**2)
y2 = np.array(100 - 150*x2 + 10*x2**2)

q = k * ((y2 - y1)/(x2 - x1))

plt.plot(x2, q)
plt.show()

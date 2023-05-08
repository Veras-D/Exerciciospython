import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-150, 150)
y = 36 * x ** 5 + 432 * x ** 4 - 13 * x ** 3 + 156 * x ** 2 + x + 12
plt.plot(x, y)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(1000) * 100
y = np.random.random(1000) * 100

plt.scatter(x, y, alpha=0.5)
plt.show()
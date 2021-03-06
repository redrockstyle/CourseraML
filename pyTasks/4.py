from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


print(optimize.differential_evolution(f, [(1, 30)]))

X = np.arange(1, 30, 0.01)
plt.plot(X, f(X))

plt.show()

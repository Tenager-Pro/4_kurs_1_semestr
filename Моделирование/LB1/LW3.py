import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math

x_1 = -2
x_2 = 0
y_1 = -1
y_2 = 1

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(x_1, x_2, 0.25)
Y = np.arange(y_1, y_2, 0.25)
X, Y = np.meshgrid(X, Y)
Z = 4*X**2 + Y**2 + 3* np.sin(X)-np.cos(Y+1)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()

levels = np.linspace(Z.min(), Z.max(), 15)

fig, ax = plt.subplots()

ax.contourf(X, Y, Z, levels=levels, cmap=cm.coolwarm, antialiased=False)
print(f"Минимум: {Z.min()}")
print(f"Максимум: {Z.max()}")
plt.show()
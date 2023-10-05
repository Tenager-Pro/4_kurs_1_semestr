import numpy as np
import matplotlib.pyplot as plt

# Определение целевой функции
def objective_function(x1, x2):
    return 2 * x1 + x2

# Определение ограничений
def constraint1(x1, x2):
    return (x1 - 2) ** 2 + (x2 - 1) ** 2 >= 4

def constraint2(x1, x2):
    return (x1 - 2) ** 2 + (x2 - 1) ** 2 <= 9

def constraint3(x1, x2):
    return x1 + x2 >= 3

    # Создание сетки значений переменных x1 и x2
x1 = np.linspace(0, 5, 500)
x2 = np.linspace(0, 5, 500)
X1, X2 = np.meshgrid(x1, x2)

# Определение целевой функции на сетке
Z = objective_function(X1, X2)

# Применение ограничений к сетке значений
constraint_mask = np.logical_and.reduce((constraint1(X1, X2), constraint2(X1, X2), constraint3(X1, X2)))
Z[~constraint_mask] = np.nan

# Нахождение точек максимума и минимума
max_idx = np.unravel_index(np.nanargmax(Z), Z.shape)
min_idx = np.unravel_index(np.nanargmin(Z), Z.shape)
max_x1, max_x2 = x1[max_idx[1]], x2[max_idx[0]]
min_x1, min_x2 = x1[min_idx[1]], x2[min_idx[0]]

# Построение графика
fig, ax = plt.subplots()
ax.contourf(X1, X2, Z, levels=50)
ax.plot([0, 5], [3, 3], 'r--', label='x1 + x2 = 3')
ax.plot([2, 2], [0, 5], 'k--', label='(x1 - 2)^2 + (x2 - 1)^2 = 4')
ax.plot([2, 2], [0, 5], 'k-', label='(x1 - 2)^2 + (x2 - 1)^2 = 9')
ax.plot(max_x1, max_x2, 'ro', label=f'Максимум: ({max_x1:.2f}, {max_x2:.2f})')
ax.plot(min_x1, min_x2, 'bo', label=f'Минимум: ({min_x1:.2f}, {min_x2:.2f})')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('График функции z=2x1 + x2')
ax.legend()
plt.show()
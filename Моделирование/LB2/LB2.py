import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return 2*x[0] + x[1]

def constraint1(x):
    return (x[0]-2)**2 + (x[1]-1)**2 - 4

def constraint2(x):
    return (x[0]-2)**2 + (x[1]-1)**2 - 9

def constraint3(x):
    return x[0] + x[1] - 3

# Задаем область значений x и y
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)

# Создаем сетку значений x и y
X, Y = np.meshgrid(x, y)

# Вычисляем значение ограничений для каждой точки сетки
Z1 = constraint1([X, Y])
Z2 = constraint2([X, Y])
Z3 = constraint3([X, Y])

# Построение графиков ограничений
plt.contourf(X, Y, Z1, [0, np.inf], colors='r', alpha=0.3, label='Constraint 1')
plt.contourf(X, Y, Z2, [0, np.inf], colors='g', alpha=0.3, label='Constraint 2')
plt.contourf(X, Y, Z3, [0, np.inf], colors='b', alpha=0.3, label='Constraint 3')

# Построение графика целевой функции
plt.contour(X, Y, objective([X, Y]), 20, cmap='jet')

# Отображение графика
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Nonlinear Programming')
plt.colorbar(label='Objective function')
plt.legend()

# Нахождение максимума и минимума в области пересечения ограничений
intersection = np.logical_and(np.logical_and(Z1>=0, Z2<=0), Z3>=0)
x_intersection = X[intersection]
y_intersection = Y[intersection]
objective_intersection = objective([x_intersection, y_intersection])
max_index = np.argmax(objective_intersection)
min_index = np.argmin(objective_intersection)
max_x = x_intersection[max_index]
max_y = y_intersection[max_index]
min_x = x_intersection[min_index]
min_y = y_intersection[min_index]
plt.scatter(max_x, max_y, color='m', marker='*', s=100, label='Maximum')
plt.scatter(min_x, min_y, color='k', marker='o', s=100, label='Minimum')

plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    a11 = 2.5
    a12 = 0.5
    a22 = 2
    a13 = -2.5
    a23 = -5.25

    return a11 * x**2 + 2 * a12 * x * y + a22 * y**2 + 2 * a13 * x + 2 * a23 * y


def grad(x, y):
    a11 = 2.5
    a12 = 0.5
    a22 = 2
    a13 = -2.5
    a23 = -5.25

    grad_x = 2 * a11 * x + 2 * a12 * y + 2 * a13
    grad_y = 2 * a12 * x + 2 * a22 * y + 2 * a23

    return np.array([grad_x, grad_y])


def hessian(x, y):
    a11 = 2.5
    a12 = 0.5
    a22 = 2

    hess_xx = 2 * a11
    hess_xy = 2 * a12
    hess_yy = 2 * a22
    return np.array([[hess_xx, hess_xy], [hess_xy, hess_yy]])


def line_search(x, y, grad, direction):
    t = 1.0
    alpha = 0.5
    beta = 0.8

    while f(x + t * direction[0], y + t * direction[1]) > f(x, y) + alpha * t * np.dot(grad, direction):
        t *= beta

    return t


def newton_method(x0, y0, epsilon):
    x_current = np.array([x0, y0])
    iteration = 0

    while True:
        iteration += 1

        grad_current = grad(x_current[0], x_current[1])
        hessian_current = hessian(x_current[0], x_current[1])

        direction = -np.linalg.inv(hessian_current) @ grad_current

        t = line_search(x_current[0], x_current[1], grad_current, direction)

        x_next = x_current + t * direction

        if np.linalg.norm(x_next - x_current) < epsilon:
            break

        x_current = x_next

    return x_next, iteration


# Начальная точка
x0 = 0
y0 = 0

# Точность
epsilon = 1e-6

# Запуск метода Ньютона
solution, iteration = newton_method(x0, y0, epsilon)

# Результат
x_min, y_min = solution
min_value = f(x_min, y_min)

print("Минимум функции:")
print("x =", x_min)
print("y =", y_min)
print("f(x, y) =", min_value)
print("Количество итераций:", iteration)

# Построение графика функции
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.scatter(x_min, y_min, min_value, color='red', label='Минимум')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()

plt.show()
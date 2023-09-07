import matplotlib.pyplot as plt
import numpy as np
from math import cos

# Заданные значения
x1 = 0
x2 = 3
e = 0.0001
n = 250


def f(x):
    return -1**n*(cos(2*n*x)/n**3)

# Метод минимизации "Деление отрезка пополам"


# Построение графика функции на заданном отрезке
x = np.linspace(x1, x2, 100)
y = f(x)


def bisection_method(f, a, b, epsilon):
    iterations = 0
    while abs(b - a) > epsilon:
        c = (a + b) / 2  # Вычисляем середину отрезка [a, b]
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    # Находим точку экстремума как середину полученного отрезка
    extremum = (a + b) / 2
    return extremum, iterations


plt.plot(x, y, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Вызов метода минимизации "Деление отрезка пополам"
minim, min_iters = bisection_method(f, x1, x2, epsilon)
maxim, max_iters = bisection_method(lambda x: -f(x), x1, x2, epsilon)

print("Минимум функции:", minim)
print("Количество итераций для минимума:", min_iters)
print("Максимум функции:", maxim)
print("Количество итераций для максимума:", max_iters)

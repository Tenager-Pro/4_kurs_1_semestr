# import math
# import matplotlib.pyplot as plt

# # Определяем функцию
# def f(x, n):
#     return (-1)**n * (math.cos(2*n*x) / n**3)

# # Определяем метод минимизации деления отрезка пополам
# def bisection_method(f, a, b, eps):
#     while (b - a) / 2 > eps:
#         c = (a + b) / 2
#         if f(c) == 0:
#             return c
#         elif f(c) * f(a) < 0:
#             b = c
#         else:
#             a = c
#     return (a + b) / 2

# # Задаем параметры
# n = 250
# a = 0
# b = 3
# eps = 0.0001

# # Строим график функции
# x_values = [i / 100 for i in range(301)]
# y_values = [f(x, n) for x in x_values]
# plt.plot(x_values, y_values)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Graph of f(x)')
# plt.show()

# # Ищем минимумы и максимумы функции
# min_values = []
# max_values = []
# for i in range(1, 301):
#     a = (i - 1) / 100
#     b = i / 100
#     if f(a, n) < f(b, n):
#         min_value = bisection_method(lambda x: f(x, n), a, b, eps)
#         min_values.append(min_value)
#     elif f(a, n) > f(b, n):
#         max_value = bisection_method(lambda x: -f(x, n), a, b, eps)
#         max_values.append(max_value)

# # Выводим результаты
# print('Минимумы функции:', min_values)
# print('Максимумы функции:', max_values)

import math
import matplotlib.pyplot as plt

def f(x, n):
    return math.pow(-1, n) * (math.cos(2 * n * x) / math.pow(n, 3))

def minimize(a, b, n, tolerance):
    minX = a
    minY = f(a, n)
    maxX = b
    maxY = f(b, n)

    while b - a > tolerance:
        m = (a + b) / 2
        fA = f(a, n)
        fB = f(b, n)
        fM = f(m, n)

        if fM > fB:
            a = m
            minX = a
            minY = fA
        else:
            b = m
            maxX = b
            maxY = fB
      
    return minX, minY, maxX, maxY

n = 250
tolerance = 0.0001

x = [i/100 for i in range(301)]  # Создаем список значений x на отрезке [0, 3]
y = [f(i, n) for i in x]  # Вычисляем соответствующие значения функции f(x)

# Строим график
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График f(x)')
plt.grid(True)
plt.show()

# Находим минимумы и максимумы
minX, minY, maxX, maxY = minimize(0, 3, n, tolerance)
print(minY)
print(maxY)
print(f"Минимум: ({minX:.4f}, {min(y)})")
print(f"Максимум: ({maxX:.4f}, {max(y)})")
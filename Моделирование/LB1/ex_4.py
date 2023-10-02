import numpy as np
import matplotlib.pyplot as plt

# Задаем коэффициенты квадратичной функции
a11 = 2.5
a12 = 0.5
a22 = 2
a13 = -2.5
a23 = -5.25

# Определяем функцию и ее производные
def f(x, y):
    return a11*x**2 + 2*a12*x*y + a22*y**2 + 2*a13*x + 2*a23*y

def df_dx(x, y):
    return 2*a11*x + 2*a12*y + 2*a13

def df_dy(x, y):
    return 2*a12*x + 2*a22*y + 2*a23

def d2f_dx2(x, y):
    return 2*a11

def d2f_dy2(x, y):
    return 2*a22

def d2f_dxdy(x, y):
    return 2*a12

# Инициализируем начальное приближение и точность
x0 = np.array([1, 1])
e = 1e-6
iter_count = 0

# Выполняем итерации метода Ньютона до достижения заданной точности
while True:
    iter_count += 1
    
    # Вычисляем градиент и гессиан функции в текущей точке
    grad = np.array([df_dx(x0[0], x0[1]), df_dy(x0[0], x0[1])])
    hess = np.array([[d2f_dx2(x0[0], x0[1]), d2f_dxdy(x0[0], x0[1])],
                     [d2f_dxdy(x0[0], x0[1]), d2f_dy2(x0[0], x0[1])]])
    
    # Вычисляем направление спуска и длину шага
    p = -np.linalg.solve(hess, grad)
    alpha = 1
    
    # Выполняем линейный поиск шага
    while np.any(f(x0 + alpha*p[0], x0 + alpha*p[1]) > f(x0[0], x0[1]) + 0.5*alpha*np.dot(grad, p)):
        alpha /= 2
    
    # Вычисляем новое приближение и проверяем точность
    x1 = x0 + alpha*p
    if np.linalg.norm(x1 - x0) < e:
        break
    else:
        x0 = x1

# Выводим результаты и график функции
print("Minimum found at x =", x1)
print("Number of iterations:", iter_count)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig, ax = plt.subplots()
ax.contour(X, Y, Z, levels=20)
ax.plot(x1[0], x1[1], 'ro')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Contour plot of f(x,y)')
plt.show()
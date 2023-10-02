import math, numpy
import matplotlib.pyplot as plt

f = lambda x: 2**x - numpy.log(x)
a = 0.1
b = 3
eps = 10**-6

df = lambda x: 2**x*numpy.log(2) - (1/x)
d2f = lambda x: 2**x*(numpy.log(2)**2) + (1/x**2)

x = (a + b) / 2

err = None
n = 0
while err == None or err > eps:
    if err == None:
        err = abs(df(x))
        continue
    err = abs(df(x))
    x = x - df(x)/d2f(x)
    n += 1

print(f"x = {x:.6f}; f(x) = {f(x):.6f}; n = {n}")

X = numpy.linspace(a, b, int((b-a)*10))
Y = [f(x) for x in X]
plt.plot(X, Y)
plt.plot(x, f(x), 'ro', label='Минимум функции')
plt.legend()
plt.show()
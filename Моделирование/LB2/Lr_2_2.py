from sympy import symbols, Eq, cos, sin, solve

# Определение символов
x1, x2, l = symbols('x1 x2 l')

# Определение функции и ограничения
f = x1 + 2*x2
constraint = x1**2 + x2**2 - 1

# Определение уравнений с помощью метода множителей Лагранжа
equation1 = Eq(f - l * constraint, 0)
equation2 = Eq(constraint, 0)

# Решение системы уравнений
solution = solve((equation1, equation2), (x1, x2, l))

# Вывод результатов

# Проверка существования экстремума
if not solution:
    print("Экстремум не существует.")
else:
    # Итерация по всем найденным решениям
    for i in range(len(solution)):
        # Вывод результата
        print("Экстремум достигается в точке:")
        print("x1 =", solution[i][0].evalf())
        print("x2 =", solution[i][1].evalf())
        print("Значение функции в экстремуме:")
        print("z =", f.subs({x1: solution[i][0], x2: solution[i][1]}).evalf())
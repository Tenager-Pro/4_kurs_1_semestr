from scipy.optimize import linprog

# Целевая функция
c = [-1500, -1000]  # Коэффициенты целевой функции

# Матрица ограничений
A = [[-1, 0], [0, -1], [1, 1]]  # Коэффициенты левых частей ограничений
b = [-10, -10, 30]  # Правые части ограничений

# Пределы переменных
x_bounds = [(10, None), (10, None)]  # [(минимальное значение п, None), (минимальное значение г, None)]

# Решение задачи линейного программирования
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Вывод результатов
if result.success:
    practice_courses = result.x[0]
    humanities_courses = result.x[1]
    faculty_income = -(result.fun)  # Минус перед fun, так как scipy минимизирует, а нам нужно максимизировать доход

    print("Оптимальная структура курсов:")
    print("Количество практических курсов:", practice_courses)
    print("Количество гуманитарных курсов:", humanities_courses)
    print("Доход факультета:", faculty_income)
else:
    print("Не удалось найти оптимальное решение.")
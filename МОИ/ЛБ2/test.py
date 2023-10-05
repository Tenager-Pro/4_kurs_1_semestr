import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
import csv
from prettytable import PrettyTable
from scipy.stats import norm, gaussian_kde
array = []
gap_number = 7

def read_csv(filename):
    with open(filename,encoding='utf-8') as read_f:
        file_reader = csv.reader(read_f)
        for row in file_reader:
            array.append(float(row[0]))

read_csv("Test9.csv")
def numbers_in_gap(array,start,end):
    result = 0
    for i in range(len(array)):
        if(array[i] >= start and array[i] < end):
            result +=1
    return result
def draw_table(left_board,right_board,n_array,midpoints):
    global gap_number
    table = PrettyTable()
    columns = ["№ промежутка", "Левая граница","Правая граница", "n", "Средняя точка промежутка" ] # Здесь у нас один заголовок, который содержит две части
    table.add_column(columns[0],[i for i in range(1,gap_number + 1,1)])
    table.add_column(columns[1],left_board)
    table.add_column(columns[2],right_board)
    table.add_column(columns[3],n_array)
    table.add_column(columns[4],midpoints)
    print(table)
def draw_first_graph(x_points,y_points):
    global array
    x = x_points
    y = y_points
    plt.subplot(1, 2, 1)
    plt.plot(x, y, color='blue', label='Полигон частот')
    plt.title('Сравнение гистограммы и полигона частот')
    plt.hist(array, bins=10, label='Гистограмма частот', color='yellowgreen')
    x_axis = np.arange(-34, 260, 1)
    y_axis = norm.pdf(x_axis, 0, 4) * 1200
 #plt.plot(x_axis, y_axis, color='red',label='Нормальное распределение' )
    plt.legend()
 # plt.show()
def draw_second_graph():
 global array
 plt.subplot(1, 2, 2)
 # Гистограмма
 plt.hist(array, bins=20, density=True, alpha=0.6, color='b', 
edgecolor='black')
 # Параметрическая оценка плотности
 x = np.linspace(min(array), max(array), 100)
 plt.plot(x, norm.pdf(x, loc=np.mean(array), 
scale=np.std(array)), 'g--', label='Параметрическая оценка')
 # Ядерная усредненная оценка
 kde = gaussian_kde(array)
 plt.plot(x, kde(x), 'm-', label='Усредненная ядерная 
оценка',color='red')
 plt.legend()
 plt.show()
# Первоначальные данные
min_Array = min(array)
max_Array = max(array)
h = (max_Array - min_Array) / gap_number
left_board = [h*i + min_Array for i in range(gap_number)]
right_board = [h*i + min_Array for i in range(1,gap_number + 1,1)]
midpoints = [(left_board[i] + right_board[i]) / 2 for i in 
range(gap_number)]
n_array = [numbers_in_gap(array,left_board[i],right_board[i]) for i 
in range(gap_number)]
# Вывод таблицы
draw_table(left_board,right_board, n_array,midpoints)
# Построение гистограммы и графика
draw_first_graph(midpoints,n_array)
# Выборочные характеристики положения и рассеивания
# Положения
# Выборочное среднее
average = sum(array) / len(array)
# Медиана
median = sum(sorted(array)[int(len(array) / 2) - 1:int(len(array) / 
2) + 1]) / 2
# Мода
moda = statistics.mode(array)
print("Выборочное среднее значение: ", average)
print("Медиана: ", median)
print("Мода : ", moda)
# Рассеивание
# Дисперсия
variace = statistics.variance(array)
# Среднеквадратичное отклонение
stan_deviation = math.sqrt(variace)
# Ошибка средней арифметической
mistake_average = stan_deviation / len(array)
# Коэффициент вариации
ratio_variation = stan_deviation / average
print("Дисперсия: ", variace)
print("Срелнеквадратичное отклоение: ", stan_deviation)
print("Ошибка средней арифметической: ", mistake_average)
print("Коэффициент вариации: ", ratio_variation)
draw_second_graph()
kde = gaussian_kde(array)
# Значения оценок в средних точках промежутков
parametric_estimate = norm.pdf(midpoints, loc=np.mean(array), 
scale=np.std(array))
kde_estimate = kde(midpoints)
table = PrettyTable()
table.add_column("#", [i for i in range(1, gap_number+1)])
table.add_column("Center", midpoints)
table.add_column("Parametric", parametric_estimate)
table.add_column("KDE", kde_estimate)
table.add_column("(fуя - fг)^2", pow((parametric_estimate -
midpoints),2))
table.add_column("(fп - fг)^2", pow((kde_estimate - midpoints),2))
print("Значения оценок в средних точках:")
print(table)

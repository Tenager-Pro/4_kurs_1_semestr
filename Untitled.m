% Заданные параметры
N = 10000; % Количество отсчетов

% Генерация отсчетов с равномерным распределением в интервале [1, 2]
alpha = rand(1, N) + 1;

% Вывод гистограммы
figure;
hist(alpha, 100); % 100 интервалов на гистограмме

% График плотности вероятности f(x)
x = linspace(1, 2, 100); % Число точек на графике плотности вероятности
f = 95.5 .* ones(100); % Функция плотности вероятности f(x)

hold on;
plot(x, f, 'r', 'LineWidth', 2); % Построение графика плотности вероятности

xlabel('x', 'FontSize', 14);
ylabel('f(x)', 'FontSize', 14);
title('Гистограмма и график плотности вероятности', 'FontSize', 16);
legend('Гистограмма', 'Плотность вероятности');

% Вычисление статистических характеристик
meanValue = mean(alpha); % Выборочное среднее
medianValue = median(alpha); % Медиана
lowerQuantile = quantile(alpha, 0.25); % Верхний квартиль
upperQuantile = quantile(alpha, 0.75); % Верхний квартиль
variance = var(alpha); % Выборочная дисперсия
stdDeviation = std(alpha); % Стандартное отклонение

% Вывод результатов
fprintf('Выборочное среднее значение: %.4f\n', meanValue);
fprintf('Медиана: %.4f\n', medianValue);
fprintf('Нижний квартиль: %.4f\n', lowerQuantile);
fprintf('Верхний квартиль: %.4f\n', upperQuantile);
fprintf('Выборочная дисперсия: %.4f\n', variance);
fprintf('Стандартное отклонение: %.4f\n', stdDeviation);
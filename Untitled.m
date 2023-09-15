% �������� ���������
N = 10000; % ���������� ��������

% ��������� �������� � ����������� �������������� � ��������� [1, 2]
alpha = rand(1, N) + 1;

% ����� �����������
figure;
hist(alpha, 100); % 100 ���������� �� �����������

% ������ ��������� ����������� f(x)
x = linspace(1, 2, 100); % ����� ����� �� ������� ��������� �����������
f = 95.5 .* ones(100); % ������� ��������� ����������� f(x)

hold on;
plot(x, f, 'r', 'LineWidth', 2); % ���������� ������� ��������� �����������

xlabel('x', 'FontSize', 14);
ylabel('f(x)', 'FontSize', 14);
title('����������� � ������ ��������� �����������', 'FontSize', 16);
legend('�����������', '��������� �����������');

% ���������� �������������� �������������
meanValue = mean(alpha); % ���������� �������
medianValue = median(alpha); % �������
lowerQuantile = quantile(alpha, 0.25); % ������� ��������
upperQuantile = quantile(alpha, 0.75); % ������� ��������
variance = var(alpha); % ���������� ���������
stdDeviation = std(alpha); % ����������� ����������

% ����� �����������
fprintf('���������� ������� ��������: %.4f\n', meanValue);
fprintf('�������: %.4f\n', medianValue);
fprintf('������ ��������: %.4f\n', lowerQuantile);
fprintf('������� ��������: %.4f\n', upperQuantile);
fprintf('���������� ���������: %.4f\n', variance);
fprintf('����������� ����������: %.4f\n', stdDeviation);
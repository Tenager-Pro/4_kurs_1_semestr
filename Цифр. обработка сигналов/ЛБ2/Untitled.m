N = 26;
f = inline('14*cos(5*t)');
T = 2*pi/5;
h = T/(N - 1);
X = 0:h:T;
F = f(X);
subplot(2, 1, 1);
F1 = F;
F2 = F;
for k = 1:(N) 
    if mod(k, 2) == 0 
        F1(k)= 0; 
    end
    plot(X, F1); 
end
stem(X, F1); grid;
axis([0 T -15 15]);
legend('Нечетные выборки');
subplot(2, 1, 2);
for k = 1:(N) 
    if mod(k, 2) ~= 0 
        F2(k) = 0; 
    end
    plot(X,F2); 
end
stem(X, F2); grid;
axis([0 T -15 15])
legend('Четные выборки');

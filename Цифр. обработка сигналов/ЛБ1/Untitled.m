N = 14; 
t = -3:0.01:3;
A = 5; 
T = 3; 
nh =(1:N) * 2-1;                            % Номера ненулевых гармоник 
harmonics = cos((2*pi*nh)'*t/T);            %
Am = 8*A /(pi*pi)./(nh.^2);                 % Амплитуды гармоник 
s = harmonics .* repmat(Am', 1, length(t)); % Строки - частичные суммы гармоник
s = cumsum(s); 
for k=1:N 
    subplot(5, 3, k);
    plot(t, s(k,:));
end



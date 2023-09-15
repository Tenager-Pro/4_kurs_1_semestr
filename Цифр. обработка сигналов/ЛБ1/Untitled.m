N = 14; 
t = -3:0.01:3;
A = 5; 
T = 3; 
nh =(1:N) * 2-1;                            % ������ ��������� �������� 
harmonics = cos((2*pi*nh)'*t/T);            %
Am = 8*A /(pi*pi)./(nh.^2);                 % ��������� �������� 
s = harmonics .* repmat(Am', 1, length(t)); % ������ - ��������� ����� ��������
s = cumsum(s); 
for k=1:N 
    subplot(5, 3, k);
    plot(t, s(k,:));
end



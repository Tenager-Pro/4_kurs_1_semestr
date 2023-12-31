N=26;
f=inline('14*cos(5*t)');
T=2*pi/5;
h=T/(N-1);
X=0:h:T;
F=f(X);
n=length(F);
subplot(2, 1, 1);
for k=1:(N)
 F1(k)=(F(k)+F(N-k+1))/2;
end
stem(X,F1);
axis([0 T -15 15]);
for k=1:(N)
 F2(k)=(F(k)-F(N-k+1))/2;
end
subplot(2, 1, 2);
stem(X,F2);
axis([0 T -15 15]);
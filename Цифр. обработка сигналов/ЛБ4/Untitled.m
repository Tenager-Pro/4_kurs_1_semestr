amp = 0.1;
step = 0.001;
t = (0:step:0.2);
 
freq1 = 20;
freq2 = 50;
freq3 = 60;
Rs = 40;
Rp = 0.1;
s1 = amp*sin(2*pi*freq1*t);
s2 = amp*sin(2*pi*freq2*t);
s3 = amp*sin(2*pi*freq3*t);
 
s = s1 + s2;
 
subplot(5, 1, 1)
plot(t, s1)
subplot(5, 1, 2)
plot(t, s2)
subplot(5, 1, 3)
plot(t, s)
 
n = 4;
 
w1 = 0.05;
w2 = 0.2;
w0 = 2 * pi * sqrt(w1 * w2);
Bw = 2 * pi * (w2 - w1);
[z, p, k] = cheb1ap(n, Rs);      
[b, a] = zp2tf(z, p, k);
 
[b1, a1] = lp2lp(b, a, w0);                  
f = abs(freqs(b1, a1, t));
subplot(5, 1, 4)
plot(t, f)
 
sf = s2 + s1.*f;
subplot(5, 1, 5)
plot(t, sf)

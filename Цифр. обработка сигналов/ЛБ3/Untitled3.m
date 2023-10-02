n = 3;
Rp = 4;
Rs = 35;
w0 = 4;
[z, p, k] = ellipap(n, Rp, Rs);     
[b, a] = zp2tf(z, p, k);        
[b1, a1] = lp2hp(b, a, w0);
w = 0:0.1:5;                    
h = freqs(b1, a1, w);
plot(w, abs(h)),

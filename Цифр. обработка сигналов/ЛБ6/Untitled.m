A=[0.2, 1, 0.7, 0.45];
w=[120, 18, 30, 60];
f=[100, 0, -60, 40];
fs = 350;
t=(1:100)/fs;
s1= A(1)*sin(2*pi*w(1)*t + f(1));
s2= A(2)*sin(2*pi*w(2)*t + f(2));
s3= A(3)*sin(2*pi*w(3)*t + f(3));
s4= A(4)*sin(2*pi*w(4)*t + f(4));
 
subplot(4,5,1);
plot(t,s1);
title('S1');
subplot(4,5,2);
plot(t,s2);
title('S2');
subplot(4,5,3);
plot(t,s3);
title('S3');
subplot(4,5,4);
plot(t,s4);
title('S4');
s=1:1;
for i=1:100
 s(i)=(s1(i)*s2(i)*s3(i)*s4(i));
end
 
subplot(4,5,5);
plot(t,s);
title('S');
sdpf = fft(s, 512);
w=(0:255)/256*(fs/2);
subplot(4,5,6);
plot(w,abs(sdpf(1:256)));
title('Frequency response S');
[pks, locs]=findpeaks((abs(sdpf(1:256))),w,'SortStr','descend');
hold on
plot(locs,pks,'x','MarkerSize',9);
hold off
locs(1:6)
 
%фильтрация гармоники с частотой 89.6484
[b,a]=ellip(6,0.1,40,[(round(locs(1)))-5 (round(locs(1)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,7);
plot(t,sf);
title(['Filtered ', num2str(locs(1))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,8);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(1))]);
 
%фильтрация гармоники с частотой 14.9414
[b,a]=ellip(6,0.1,40,[(round(locs(2)))-5 (round(locs(2)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,9);
plot(t,sf);
title(['Filtered ', num2str(locs(2))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,10);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(2))]);
 
%фильтрация гармоники с частотой 165.2344
[b,a]=ellip(6,0.1,40,[(round(locs(3)))-5 (round(locs(3)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,11);
plot(t,sf);
title(['Filtered ', num2str(locs(3))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,12);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(3))]);
 
%фильтрация гармоники с частотой 134.4727
[b,a]=ellip(6,0.1,40,[(round(locs(4)))-5 (round(locs(4)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,13);
plot(t,sf);
title(['Filtered ', num2str(locs(4))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,14);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(4))]);
 
%фильтрация гармоники с частотой 210.0586
[b,a]=ellip(6,0.1,40,[(round(locs(5)))-5 (round(locs(5)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,15);
plot(t,sf);
title(['Filtered ', num2str(locs(5))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,16);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(5))]);
 
%фильтрация гармоники с частотой 59.7656
[b,a]=ellip(6,0.1,40,[(round(locs(6)))-5 (round(locs(6)))+5]*2/fs);
[h,w]=freqz(b,a,512);
sf=filter(b,a,s);
subplot (4,5,17);
plot(t,sf);
title(['Filtered ', num2str(locs(6))]);
w=(0:255)/256*(fs/2);
sf1=fft(sf,512);
subplot (4,5,18);
plot(w,abs(sf1(1:256)'));
title(['Frequency response ', num2str(locs(6))]);

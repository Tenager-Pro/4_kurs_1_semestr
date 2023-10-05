import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from scipy.stats import gaussian_kde

def normal(x):
    return 1 / np.sqrt(2*np.pi) / np.sqrt(np.var(data)) * np.e**(-1/2 * ((x - np.mean(data)) / np.sqrt(np.var(data)))**2)

data = list()
with open("Test6.csv", "r+") as input:
    data = [float(item) for item in input.readlines()]
centers = [-13, 29, 71, 113, 155, 197, 239]
buckets = [0] * 7
for i in range(len(data)):
    if -34<data[i]<8:
        buckets[0] += 1
    elif 8<data[i]<50:
        buckets[1] += 1
    elif 50<data[i]<92:
        buckets[2] += 1
    elif 92<data[i]<134:
        buckets[3] += 1
    elif 134<data[i]<176:
        buckets[4] += 1
    elif 176<data[i]<218:
        buckets[5] += 1
    elif 218<data[i]<260:
        buckets[6] += 1
##################################
print(buckets[0])
print(buckets[1])
print(buckets[2])
print(buckets[3])
print(buckets[4])
print(buckets[5])
print(buckets[6])
plt.hist(data, bins=7, edgecolor= "black", range=(-34, 260))

# Нормализованный полигон
plt.plot(centers, [buckets[i] for i in range(len(buckets))],color= "red", label= "Polygon sample")
# Полигон приведённых частот 
plt.plot(centers, [buckets[i] for i in range(len(buckets))], color= "red", label= "Polygon sample")
##################################
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Mode: {st.mode(data)}")
print(f"R: {max(data) - min(data)}")
print(f"s^2: {np.var(data)}")
print(f"s: {np.sqrt(np.var(data))}")
print(f"V: {np.sqrt(np.var(data)) / np.mean(data) * 100}%")


x = np.linspace(-34, 260, 700)
y = [(normal(item)) for item in x]
plt.plot(x, y, color= "orange", label= "Parametric normal")
kde = gaussian_kde(data)
plt.plot(x, [(kde(item)) for item in x], color= "black", label= "KDE")
plt.legend()
plt.show()
###################################
fg = [round(buckets[i] / len(data) / -34, 260) for i in
range(len(centers))]
fya = [round(float(kde(i)), 260) for i in centers]
fp = [round(normal(i), 260) for i in centers]
fyag = [round((fya[i] - fg[i])**2, 260) for i in range(len(fg))]
fpg = [round((fp[i] - fg[i])**2, 260) for i in range(len(fg))]
print(fg)
print(fya)
print(fp)
print(fyag)
print(fpg)

import matplotlib.pyplot as plt
import numpy as np
from math import log

data = [1439, 1418, 1413, 1391, 1379, 1367, 1356, 1341, 1332, 1320, 1302, 1295, 1285, 1268, 1259, 1252, 1237, 1227, 1216, 1206, 1199, 1188, 1178, 1171, 1154, 1152, 1143, 1127, 1127, 1111, 1105, 1101, 1086, 1080, 1070, 1065, 1058, 1048, 1043, 1034, 1029, 1020, 1012, 1003, 1002, 988, 987, 977, 973, 962, 963, 950, 944, 943, 935, 926, 921, 915, 910, 904, 901, 892, 890, 882, 880, 870, 863, 864, 858, 848, 847, 844, 833, 834, 823, 827, 814, 814, 808, 800, 804, 793, 790, 784, 785, 780, 771, 770, 765, 760, 758, 752, 751, 745, 742, 739, 735, 732, 725, 720]

def gen_benford(x_0, y_0, c):
    scale = y_0 / log(1 + 1/(c * x_0))

    def benford(n):
        return scale * log(1 + 1/(c * n))

    return benford

f = gen_benford(1, data[0], 0.000103)

# print(f(99))

# X values for plotting the continuous function
x_vals = np.linspace(1, len(data), 500)
f_vals = [f(n) for n in x_vals]

# Histogram setup
fig, ax = plt.subplots(figsize=(10, 6))

# Plot histogram
ax.hist(range(1, len(data) + 1), bins=len(data), weights=data, alpha=0.6, label="Data", edgecolor='black')

# Plot the Benford-like function
ax.plot(x_vals, f_vals, color='red', label="Benford Distribution")

# Labels and legend
ax.set_title("Attempting To Fit Benford Distribution")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.legend()

plt.tight_layout()
plt.show()

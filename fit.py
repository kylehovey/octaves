import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

raw_data = [1439, 1418, 1413, 1391, 1379, 1367, 1356, 1341, 1332, 1320, 1302, 1295, 1285, 1268, 1259, 1252, 1237, 1227, 1216, 1206, 1199, 1188, 1178, 1171, 1154, 1152, 1143, 1127, 1127, 1111, 1105, 1101, 1086, 1080, 1070, 1065, 1058, 1048, 1043, 1034, 1029, 1020, 1012, 1003, 1002, 988, 987, 977, 973, 962, 963, 950, 944, 943, 935, 926, 921, 915, 910, 904, 901, 892, 890, 882, 880, 870, 863, 864, 858, 848, 847, 844, 833, 834, 823, 827, 814, 814, 808, 800, 804, 793, 790, 784, 785, 780, 771, 770, 765, 760, 758, 752, 751, 745, 742, 739, 735, 732, 725, 720]
data = [x / sum(raw_data) for x in raw_data]

offset = 100

# Create x values as indices (starting from 1 to avoid division by zero)
x_data = np.arange(offset, len(data) + offset)
y_data = np.array(data)

# Define the function to fit
def power_law(x, a, k):
    return a * x ** (-k)

# Fit the function to the data
params, covariance = curve_fit(power_law, x_data, y_data, p0=[1, 1])

# Extract fitted parameters
a_fit, k_fit = params

print(f"Fitted function: f(x) = {a_fit:.4f} * x^(-{k_fit:.4f})")

# Optional: plot the fit
x_fit = np.linspace(offset, len(data) + offset, 100)
y_fit = power_law(x_fit, a_fit, k_fit)

plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, label=f'Fit: {a_fit:.2f} * x^(-{k_fit:.2f})', color='red')
plt.xlabel('Index (x)')
plt.ylabel('Value (y)')
plt.legend()
plt.title('Power-law Fit')
plt.grid(True)
plt.show()

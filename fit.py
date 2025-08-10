import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # You need to run generate.py first
    raw_data = np.load("./buckets.npy")

    # Normalize the data
    normalized_data = raw_data / sum(raw_data)

    offset = len(normalized_data)

    # Rescale (1,2) to the bounds of the data
    x_data = np.arange(offset, 2 * offset)
    y_data = np.array(normalized_data)

    def power_law(x, a, k):
        return a * x ** (-k)

    (a_fit, k_fit), covariance = curve_fit(power_law, x_data, y_data, p0=[1, 1])

    print(f"Fitted function: f(x) = {a_fit:.4f} * x^(-{k_fit:.4f})")

    x_fit = np.linspace(offset, 2 * offset, 100)
    y_fit = power_law(x_fit, a_fit, k_fit)

    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_fit, y_fit, label=f'Fit: {a_fit:.2f} * x^(-{k_fit:.2f})', color='red')
    plt.xlabel('Index (x)')
    plt.ylabel('Normalized Value (y)')
    plt.legend()
    plt.title('Power-Law Fit')
    plt.grid(True)
    plt.show()

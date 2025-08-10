from fractions import Fraction
from math import floor, log2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

fifth = Fraction(3, 2)

# 3/2 * 3/2 = 9/4 = 2 + 1/4 -> 1/2
# 27/8 = 2 + 11/8 -> 11/4

def trans(r):
    k = floor(log2(r))
    b = 1 << k

    return (r - b) / b

destinations = {fifth}
temp = fifth

count = 1500

# Progress bar for the iteration
for _ in tqdm(range(count), desc="Generating destinations"):
    temp = temp * fifth
    destinations.add(trans(temp))

print(f"Count: {count}")
print(f"Uniques: {len(destinations)}")

fraction_values = sorted(float(f) for f in destinations)

# Histogram data
num_bins = 100
hist, bin_edges = np.histogram(fraction_values, bins=num_bins, range=(0, 1), density=False)
heatmap_data = hist.reshape(1, -1)  # For horizontal heatmap

# Create side-by-side plots
fig, axs = plt.subplots(1, 2, figsize=(14, 4), gridspec_kw={'width_ratios': [3, 1]})

# Histogram
axs[0].hist(fraction_values, bins=num_bins, range=(0, 1), edgecolor='black', color='skyblue')
axs[0].set_title("Histogram of Transposed Intervals")
axs[0].set_xlabel("Value")
axs[0].set_ylabel("Count")
axs[0].set_xlim(0, 1)

# Heatmap
im = axs[1].imshow(heatmap_data, cmap="plasma", aspect="auto", extent=[0, 1, 0, 1])
axs[1].set_title("Heatmap")
axs[1].set_xlabel("Value")
axs[1].set_yticks([])

# Colorbar for the heatmap
cbar = fig.colorbar(im, ax=axs[1], orientation='vertical', label='Count per bin')

plt.tight_layout()
plt.show()

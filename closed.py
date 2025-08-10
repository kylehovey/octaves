from math import floor, log2
import json
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

_scale = log2(3)

def f(n):
    return 3**n / 2**(floor(n*_scale)) - 1

destinations = []

count = 100000

# Progress bar for the iteration
for i in tqdm(range(count), desc="Generating destinations"):
    destinations.append(f(i))

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

print(json.dumps([int(x) for x in hist]))

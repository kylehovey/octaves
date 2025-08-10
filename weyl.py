import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from math import floor
from tqdm import tqdm

fifth = Fraction(3, 2)

def ocrem(k):
    return k - floor(k) + 1

destinations = {fifth}
temp = fifth

# Progress bar for the iteration
for _ in tqdm(range(20000), desc="Generating destinations"):
    temp = temp * fifth
    destinations.add(ocrem(temp))

# Convert to sorted list of floats
fraction_values = sorted(float(f) for f in destinations)

# Histogram data
num_bins = 10000
hist, bin_edges = np.histogram(fraction_values, bins=num_bins, range=(1, 2), density=False)
heatmap_data = hist.reshape(1, -1)  # For horizontal heatmap

# Create side-by-side plots
fig, axs = plt.subplots(1, 2, figsize=(14, 4), gridspec_kw={'width_ratios': [3, 1]})

# Histogram
axs[0].hist(fraction_values, bins=num_bins, range=(1, 2), edgecolor='black', color='skyblue')
axs[0].set_title("Histogram of Transformed Fractions")
axs[0].set_xlabel("Value")
axs[0].set_ylabel("Count")
axs[0].set_xlim(1, 2)

# Heatmap
im = axs[1].imshow(heatmap_data, cmap="plasma", aspect="auto", extent=[1, 2, 0, 1])
axs[1].set_title("Heatmap")
axs[1].set_xlabel("Value")
axs[1].set_yticks([])

# Colorbar for the heatmap
cbar = fig.colorbar(im, ax=axs[1], orientation='vertical', label='Count per bin')

plt.tight_layout()
plt.show()

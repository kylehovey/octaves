from math import floor, log2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

r = 3/2
scale = log2(r)

def f(n):
    alpha = n * scale
    alpha = alpha - floor(alpha)
    return 2**alpha - 1

destinations = []
count = 1000000
num_bins = 1000

# Change this to plot the output
plot_output = False

if __name__ == "__main__":
    # Progress bar for the iteration
    for i in tqdm(range(count), desc="Generating destinations"):
        destinations.append(f(i))

    print(f"Count: {count}")
    print(f"Uniques: {len(destinations)}")

    fraction_values = sorted(float(x) for x in destinations)

    # Histogram data
    hist, bin_edges = np.histogram(fraction_values, bins=num_bins, range=(0, 1), density=False)
    heatmap_data = hist.reshape(1, -1)  # For horizontal heatmap

    np.save("buckets.npy", hist)

    if plot_output:
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

from fractions import Fraction
from math import floor, log2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

fifth = Fraction(3, 2)

def trans(r):
    k = floor(log2(r))
    b = 1 << k

    return (r - b) / b

def closed(n):
    return 3**n / 2**(floor(n*log2(3)))

def approx(a, b, epsilon = 0.01):
    return abs(a - b) <= epsilon

destinations = {fifth}
temp = fifth

count = 1500

# Progress bar for the iteration
for i in tqdm(range(count), desc="Generating destinations"):
    temp = temp * fifth
    ours = trans(temp)
    theirs=closed(i+2) - 1

    if not approx(theirs, ours):
        print(f"Found mismatch at n={i+1}, ours={ours}, theirs={theirs}")

    destinations.add(ours)

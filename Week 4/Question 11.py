import numpy as np

rr = int(input("rows? "))
cc = int(input("cols? "))

# Create the 2D array with sequential integers
aa = np.arange(1, rr * cc + 1).reshape((rr, cc))

print("Array:\n", aa)
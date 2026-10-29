import numpy as np
from scipy.integrate import quad

# Define the function
def f(x):
    return x * np.sin(x**2)

# Limits of integration
a = 1
b = 5

# (a) Exact result using the formula
exact = (np.cos(a**2) - np.cos(b**2)) / 2

# (b) Numerical result using scipy.integrate.quad
numerical, error = quad(f, a, b)

# Print the results
print("Exact result =", exact)
print("Numerical result =", numerical)
print("Estimated numerical error =", error)
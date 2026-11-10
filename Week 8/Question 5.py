import numpy as np
from scipy.integrate import quad

# Define the function
def f(x):
    return x * np.sin(x**2)


# Trapezoid rule
def trap(f, a, b, nn):
    xs = np.linspace(a, b, nn + 1)
    h = (b - a) / nn

    weights = np.ones(nn + 1)
    weights[0] = 0.5
    weights[-1] = 0.5

    return h * sum(weights * f(xs))


# Limits of integration
a = 1
b = 5

# (a) Exact result
exact = (np.cos(a**2) - np.cos(b**2)) / 2

# (b) Numerical result using quad
numerical, error = quad(f, a, b)

print("Exact result:", exact)
print("Result using quad:", numerical)
print()

# Repeatedly ask for the number of slices
while True:
    N = int(input("Enter number of slices N (N < 1 to quit): "))

    if N < 1:
        print("Program finished.")
        break

    # (c) Trapezoid-rule result
    trapezoid = trap(f, a, b, N)

    print("Exact result:      ", exact)
    print("Result using quad: ", numerical)
    print("Trapezoid result:  ", trapezoid)
    print("Absolute error:    ", abs(trapezoid - exact))
    print()
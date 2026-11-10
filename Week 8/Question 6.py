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


# Simpson's rule
def simps(f, a, b, nn):
    if nn % 2 != 0:
        print("Simpson's rule: increasing N from", nn, "to", nn + 1)
        nn += 1

    xs = np.linspace(a, b, nn + 1)
    h = (b - a) / nn

    weights = np.full(nn + 1, 4.0)
    weights[::2] = 2.0
    weights[0] = 1.0
    weights[-1] = 1.0

    return (h / 3) * sum(weights * f(xs))


# Limits of integration
a = 1
b = 5

# Exact result
exact = (np.cos(a**2) - np.cos(b**2)) / 2

# Numerical result using quad
numerical, error = quad(f, a, b)

print("Exact result:     ", exact)
print("Result using quad:", numerical)
print()

# Ask for N repeatedly
while True:
    N = int(input("Enter number of slices N (N < 1 to quit): "))

    if N < 1:
        print("Program finished.")
        break

    trapezoid = trap(f, a, b, N)
    simpson = simps(f, a, b, N)

    print("Exact result:      ", exact)
    print("Result using quad: ", numerical)
    print("Trapezoid result:  ", trapezoid)
    print("Simpson result:    ", simpson)
    print("Trapezoid error:   ", abs(trapezoid - exact))
    print("Simpson error:     ", abs(simpson - exact))
    print()
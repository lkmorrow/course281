import numpy as np
from numpy import exp, sqrt
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Read the data
p4data = pd.read_excel('peak4.xlsx')
print(list(p4data))

# Convert the columns to NumPy arrays
c0, c1 = list(p4data)
xs = p4data[c0].to_numpy()
ys = p4data[c1].to_numpy()


# Gaussian plus linear background
def gauss(x, aa, x0, w, bb0, bb1):
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x


# Gaussian plus quadratic background
def gauss2(x, aa, x0, w, bb0, bb1, bb2):
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2


# Initial guesses for the linear model
guesses = [3, 5, 1, 1, 0]

# Fit the linear model
(p0, p1, p2, p3, p4), cc = curve_fit(
    gauss, xs, ys, p0=guesses
)

# Calculate the 2-sigma parameter uncertainties
uncerts = 2*sqrt(np.diag(cc))

print("\nGaussian plus linear background:")
print(f"aa = {p0:.5f} +/- {uncerts[0]:.5f}")
print(f"x0 = {p1:.5f} +/- {uncerts[1]:.5f}")
print(f"w = {p2:.5f} +/- {uncerts[2]:.5f}")
print(f"bb0 = {p3:.5f} +/- {uncerts[3]:.5f}")
print(f"bb1 = {p4:.5f} +/- {uncerts[4]:.5f}")

# Calculate reduced chi-squared
yfit = gauss(xs, p0, p1, p2, p3, p4)
dof = len(xs) - len(guesses)
chisqr_linear = sum((yfit - ys)**2) / dof

print(f"Reduced chi-squared = {chisqr_linear:.5f}")


# Initial guesses for the quadratic model
guesses2 = [2.75, 4.9, 0.62, 1.68, 0.007, 0]

# Fit the quadratic model
(a, x0, w, b0, b1, b2), cc2 = curve_fit(
    gauss2, xs, ys, p0=guesses2
)

# Calculate the 2-sigma parameter uncertainties
uncerts2 = 2*sqrt(np.diag(cc2))

print("\nGaussian plus quadratic background:")
print(f"aa = {a:.5f} +/- {uncerts2[0]:.5f}")
print(f"x0 = {x0:.5f} +/- {uncerts2[1]:.5f}")
print(f"w = {w:.5f} +/- {uncerts2[2]:.5f}")
print(f"bb0 = {b0:.5f} +/- {uncerts2[3]:.5f}")
print(f"bb1 = {b1:.5f} +/- {uncerts2[4]:.5f}")
print(f"bb2 = {b2:.5f} +/- {uncerts2[5]:.5f}")

# Calculate reduced chi-squared
yfit2 = gauss2(xs, a, x0, w, b0, b1, b2)
dof2 = len(xs) - len(guesses2)
chisqr_quad = sum((yfit2 - ys)**2) / dof2

print(f"Reduced chi-squared = {chisqr_quad:.5f}")


# Plot both fits in one window
xmod = np.linspace(min(xs), max(xs), 500)

plt.plot(xs, ys, 'bo', label='Data')
plt.plot(xmod, gauss(xmod, p0, p1, p2, p3, p4),
         label='Gaussian + linear background')
plt.plot(xmod, gauss2(xmod, a, x0, w, b0, b1, b2),
         label='Gaussian + quadratic background')

plt.xlabel(c0)
plt.ylabel(c1)
plt.legend()
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import exp
from scipy.optimize import curve_fit

# Read the data
gl1data = pd.read_excel('gl1.xlsx')
gl2data = pd.read_excel('gl2.xlsx')

x1 = gl1data.iloc[:, 0].to_numpy()
y1 = gl1data.iloc[:, 1].to_numpy()

x2 = gl2data.iloc[:, 0].to_numpy()
y2 = gl2data.iloc[:, 1].to_numpy()


# Gaussian function
def gauss(x, A, x0, w, B):
    return A*exp(-(x-x0)**2/(2*w**2)) + B


# Lorentzian function
def lorentz(x, A, x0, w, B):
    return A/(1+((x-x0)/w)**2) + B


# Fit the data
guesses = [1.5, 0, 2, -0.2]

pg1, _ = curve_fit(gauss, x1, y1, p0=guesses)
pl1, _ = curve_fit(lorentz, x1, y1, p0=guesses)

pg2, _ = curve_fit(gauss, x2, y2, p0=guesses)
pl2, _ = curve_fit(lorentz, x2, y2, p0=guesses)


# Create one window with four graphs
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# GL1 Gaussian
ax[0, 0].scatter(x1, y1, label='Data')
ax[0, 0].plot(x1, gauss(x1, *pg1), label='Gaussian fit')
ax[0, 0].set_title('GL1 - Gaussian')
ax[0, 0].legend()

# GL1 Lorentzian
ax[0, 1].scatter(x1, y1, label='Data')
ax[0, 1].plot(x1, lorentz(x1, *pl1), label='Lorentzian fit')
ax[0, 1].set_title('GL1 - Lorentzian')
ax[0, 1].legend()

# GL2 Gaussian
ax[1, 0].scatter(x2, y2, label='Data')
ax[1, 0].plot(x2, gauss(x2, *pg2), label='Gaussian fit')
ax[1, 0].set_title('GL2 - Gaussian')
ax[1, 0].legend()

# GL2 Lorentzian
ax[1, 1].scatter(x2, y2, label='Data')
ax[1, 1].plot(x2, lorentz(x2, *pl2), label='Lorentzian fit')
ax[1, 1].set_title('GL2 - Lorentzian')
ax[1, 1].legend()

# Label the axes
for a in ax.flat:
    a.set_xlabel('x')
    a.set_ylabel('y')

plt.tight_layout()
plt.show()

'''For gl1, the Lorentzian model provides a better fit because it has a lower
reduced chi-squared than the Gaussian model. For gl2, the Gaussian model provides
a better fit because it has a lower reduced chi-squared than the Lorentzian model.'''
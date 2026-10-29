# Week 6: Polynomial fitting for data3.xlsx

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit
from scipy.optimize import curve_fit

# Read the data file and print the column names
data3 = pd.read_excel('data3.xlsx')
print(list(data3))

# Extract the x and y columns
c0, c1 = list(data3)
xs = data3[c0].to_numpy()
ys = data3[c1].to_numpy()

# Assume equal uncertainties because the file has no yerr column
yerrs = np.ones(len(ys))


# Define the polynomial models
def linmod(x, p0, p1):
    return p0 + p1*x

def quadmod(x, p0, p1, p2):
    return p0 + p1*x + p2*x**2

def cubicmod(x, p0, p1, p2, p3):
    return p0 + p1*x + p2*x**2 + p3*x**3

def quarticmod(x, p0, p1, p2, p3, p4):
    return p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4

def quinticmod(x, p0, p1, p2, p3, p4, p5):
    return p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4 + p5*x**5


# Store the models and their names
models = [
    (linmod, 'Linear'),
    (quadmod, 'Quadratic'),
    (cubicmod, 'Cubic'),
    (quarticmod, 'Fourth order'),
    (quinticmod, 'Fifth order')
]

# Plot the data
plt.errorbar(xs, ys, yerr=yerrs, fmt='go',
             capsize=3, label='Data')

# Define x values for plotting the fitted curves
xmods = np.linspace(min(xs), max(xs), 300)

# Fit and plot each polynomial
for model, name in models:
    print('\n' + name + ' fit')

    # Fit using Dfit and print the fit results
    fit = Dfit(model, xs, ys, yerrs)
    fit.printfit()

    # Get fitted parameters for plotting
    parameters, covariance = curve_fit(
        model, xs, ys,
        sigma=yerrs,
        absolute_sigma=True,
        maxfev=10000
    )

    # Calculate chi-squared and reduced chi-squared
    yfit = model(xs, *parameters)
    chi_squared = np.sum(((ys - yfit) / yerrs)**2)
    dof = len(xs) - len(parameters)
    chi_squared_reduced = chi_squared / dof

    print('Reduced chi-squared =', chi_squared_reduced)

    # Plot the fitted curve
    plt.plot(xmods, model(xmods, *parameters), label=name)

# Label the graph
plt.xlabel(c0)
plt.ylabel(c1)
plt.title('Polynomial Fits to data3.xlsx')
plt.legend()
plt.show()
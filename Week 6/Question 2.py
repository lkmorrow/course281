import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the data from the Excel file
data = pd.read_excel("data2.xlsx")

# Get the x, y and uncertainty values
x = data["x (cm)"].to_numpy()
y = data["y (micro-m)"].to_numpy()
yerr = data["yerr"].to_numpy()

# Define a polynomial model
def polynomial(x, *parameters):
    return np.polyval(parameters, x)

# Plot the measured data
plt.errorbar(x, y, yerr=yerr, fmt='o', label='Data')

# Try polynomial orders 1 through 5
for order in range(1, 6):

    # Fit the polynomial to the data
    parameters, covariance = curve_fit(
        polynomial,
        x,
        y,
        p0=np.zeros(order + 1),
        sigma=yerr,
        absolute_sigma=True
    )

    # Calculate the uncertainties in the parameters
    uncertainties = np.sqrt(np.diag(covariance))

    # Calculate the chi-squared value
    y_fit = polynomial(x, *parameters)
    chi_squared = np.sum(((y - y_fit) / yerr)**2)

    # Calculate the reduced chi-squared value
    degrees_of_freedom = len(x) - (order + 1)
    chi_squared_reduced = chi_squared / degrees_of_freedom

    # Print the results
    print("\nPolynomial order:", order)

    for i in range(len(parameters)):
        print("Parameter", i + 1, "=", parameters[i],
              "+/-", uncertainties[i])

    print("Reduced chi-squared =", chi_squared_reduced)

    # Plot the fitted polynomial
    x_line = np.linspace(min(x), max(x), 300)
    y_line = polynomial(x_line, *parameters)

    plt.plot(x_line, y_line, label="Order " + str(order))

# Finish the plot
plt.xlabel("x (cm)")
plt.ylabel("y (micro-m)")
plt.title("Polynomial Fits to Data")
plt.legend()
plt.show()
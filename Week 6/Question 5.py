import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import exp
from dfit import Dfit

# Read the data from the Excel file
p4data = pd.read_excel('peak4.xlsx')

# Get the column names
print(list(p4data))
c0, c1 = list(p4data)

# Store the x and y data
xs = p4data[c0].to_numpy()
ys = p4data[c1].to_numpy()

# Gaussian plus quadratic background
def gauss2(x, aa, x0, w, bb0, bb1, bb2):
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2

# Initial guesses for the six parameters
guesses = [2.5, 4.9, 0.6, 1.7, 0.01]

# Fit the data
p4fit2 = Dfit(gauss2, xs, ys, p0s=guesses)

# Plot the fit
p4fit2.plotfit(xlabel=c0, ylabel=c1)

# Print the fit results
p4fit2.printfit()

plt.show()

'''Determine whether or not using this additional parameter is justified.'''

'''Adding a quadratic term to the background improves the fit.
The fitted value of the additional parameter is b_2 = 0.019208 ± 0.0069493.
Since the value is approximately 2.76 times its uncertainty, it is
significantly different from zero. Therefore, the additional parameter appears
to be justified, as the quadratic background provides a better description of the data.'''
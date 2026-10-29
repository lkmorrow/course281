# Gaussian plus linear background fit to peak4.xlsx

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import exp
from dfit import Dfit

# Read the data
p4data = pd.read_excel('peak4.xlsx')
print(list(p4data))

# Convert the columns to Numpy arrays
c0, c1 = list(p4data)
xs = p4data[c0].to_numpy()
ys = p4data[c1].to_numpy()

# Define the Gaussian plus linear background model
def gauss(x, aa, x0, w, bb0, bb1):
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x

# First fit: use the guesses from the handout
guesses = [3, 5, 1, 1, 0]

p4fit = Dfit(gauss, xs, ys, p0s=guesses)
p4fit.plotfit(xlabel=c0, ylabel=c1)
p4fit.printfit()

# Second fit: change all guesses to one
#guesses = [1, 1, 1, 1, 1]
#guesses = [1, 2, 3, 4, 5] works
#guesses = [2, 3, 6, 7, 5] leads to error
guesses = [2.5, 4.5, 0.2, 1.7, 0.01] #works

p4fit2 = Dfit(gauss, xs, ys, p0s=guesses)
p4fit2.plotfit(xlabel=c0, ylabel=c1)
p4fit2.printfit()

plt.show()

'''Some number combinations cause it to error. Unsure of what the pattern is.
Decimal places can be changed without much impact.'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dfit import Dfit

# Read the data
decay1 = pd.read_excel('decay1.xlsx')
decay2 = pd.read_excel('decay2.xlsx')

t1 = decay1.iloc[:, 0].to_numpy()
N1 = decay1.iloc[:, 1].to_numpy()

t2 = decay2.iloc[:, 0].to_numpy()
N2 = decay2.iloc[:, 1].to_numpy()

# Radioactive decay model
def decay(t, N0, tau, B):
    return N0 * np.exp(-t / tau) + B

# Fit all three parameters
fit1a = Dfit(decay, t1, N1,
             p0s=[170, 54, 25],
             units=['cts/min', 'min', 'cts/min'])

fit2a = Dfit(decay, t2, N2,
             p0s=[220, 54, 25],
             units=['cts/min', 'min', 'cts/min'])

# Fit N0 and tau, keeping B fixed at 25
fit1b = Dfit(decay, t1, N1,
             p0s=[170, 54, 25],
             varies=[True, True, False],
             units=['cts/min', 'min', 'cts/min'])

fit2b = Dfit(decay, t2, N2,
             p0s=[220, 54, 25],
             varies=[True, True, False],
             units=['cts/min', 'min', 'cts/min'])

# Print the fit results
print('Data set 1: all parameters fitted')
fit1a.printfit()

print('\nData set 1: B fixed at 25')
fit1b.printfit()

print('\nData set 2: all parameters fitted')
fit2a.printfit()

print('\nData set 2: B fixed at 25')
fit2b.printfit()

"""The accepted value of the decay constant is tau = 54.3 min.
For the longer data set, the fitted value of tau is reasonably
close to the accepted value whether the background B is fitted
or fixed at 25 counts/min. For the shorter data set, fitting all
three parameters gives a much larger uncertainty in tau, whereas
fixing B=25 gives a more precise result. 

This is because the shorter data set looks nearly like a straight line
on linear axes, so there is not enough information to accurately determine
all three parameters N_0, tau, and B independently. Fixing the background
leaves only two parameters to fit, improving the estimate of tau."""
# Weekx 6 demo

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

# read data file and print the column names
data1 = pd.read_excel('data1.xlsx')
print(list(data1))

# extract to arrays
c0,c1,c2 = list (data1)
xs = data1[c0].to_numpy()
ys = data1[c1].to_numpy()
yerrs = data1[c2].to_numpy()

def linmod(x,p0,p1):
    'linear model'
    return p0 + p1*x

# plot the data
#plt.plot(xs,ys,'go')
plt.errorbar(xs,ys,yerrs, fmt='go', capsize=5)
plt.xlabel(c0)
plt.xlabel(c1)
plt.xlabel(c2)

# plot the odel
xmods = np.linspace(-1,11,300)
p0 = 40.0
p1 = -2
ymods = linmod(xmods,p0,p1)
#plt.plot(xmods,ymods, 'b-')
#plt.show()

# use Dfit to fit the data
linfit = Dfit(linmod,xs,ys,yerrs)
linfit.plotfit()
linfit.printfit()
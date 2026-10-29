import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt
import pandas as pd

# define a function of two variables
def f(x,y):
    r = sqrt(x**2 + y**2)
    return cos(r)
pts = 5
xs = np.linspace(-20,20,pts)
ys = np.linspace(-20,20,pts)[:,newaxis]

print(xs)
print(ys)
fs = f(xs,ys)
print(fs)
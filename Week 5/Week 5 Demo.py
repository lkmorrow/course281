import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('gl2.xlsx')
df = pd.read_excel('gl2_missing.xlsx')
print(type(df))
print(list(df))
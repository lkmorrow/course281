"""linalg.py 10/20/26 Liam Morrow
try out fitting."""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy import linalg

#ii3 = np.eye(3)
# print(ii3)

mm = np.array(((2,1,4,1),(3,4,-1,-1),(1,-4,1,5),(2,-2,1,3)))
print(mm)
r = np.array((-4,3,9,7))
print(r)

w,x,y,z = linalg.inv(mm)@r
print(w,x,y,z)

w,x,y,z = linalg.solve(mm,r)
print(w,x,y,z)

# make 2 vectors, compute various products
# a = np.array((1,2,3))
#b = np.array((4,5,6),float)
#print(f'a = {a}     b = {b}')
#print(f'a*b = {a*b}')
#print(f'a@b = {a@b}')
#print(f'a@b = {np.dot(a,b)}')
#print(f'a cross b = {np.cross(a,b)}')

# make 2 matrices, compute various products
#aa = np.array(((1,2,3),(4,5,6)))
#bb = np.array(((5,6),(7,8),(9,10)))
#print(f'aa =\n{aa}   \nbb =\n{bb}')
#print(f'aa*bb =\n{aa*bb}')
import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun1(t, y):
    """Derivative function"""
    dydt = -y**3 * sin(t)
    return dydt

# Domain
ta = 0
tb = 10

# Initial condition
y0 = [1.0]

# Solve with solve_ivp
nnivp = 300
ts = np.linspace(ta, tb, nnivp)
t_span = ts[0], ts[-1]

sol = solve_ivp(fun1, t_span, y0, t_eval=ts)
ys = sol.y[0]

# Solve with Euler
nn = 50
tes = np.linspace(ta, tb, nn)
h = (tb - ta) / (nn - 1)

yes = np.zeros_like(tes)
yes[0] = y0[0]

for j in range(nn-1):
    tj = tes[j]
    yj = yes[j]
    yes[j+1] = yj + h * fun1(tj, yj)

# Solve with RK2
y2s = np.zeros_like(tes)
y2s[0] = y0[0]

for j in range(nn-1):
    tj = tes[j]
    yj = y2s[j]
    k1 = h * fun1(tj, yj)
    k2 = h * fun1(tj + h/2, yj + k1/2)
    y2s[j+1] = yj + k2

# Plot results
plt.figure()
plt.plot(ts, ys, label="solve_ivp")
plt.plot(tes, yes, "b.", label="Euler")
plt.plot(tes, y2s, "r.", label="RK2")

plt.legend()
plt.xlabel("t")
plt.ylabel("y")
plt.title(f"Using {nn} points")
plt.grid()

plt.show(block=True)
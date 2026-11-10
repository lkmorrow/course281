import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Circuit constants
R = 10e3
C = 1e-6

# Input voltage constants
A = 2.0
omega = 300

# Define input voltage
def Vin(t):
    return A * np.sin(omega * t)


# Define the ODE
def fun1(t, Vout):
    dVoutdt = (Vin(t) - Vout[0]) / (R * C)
    return [dVoutdt]


# Time domain
ta = 0
tb = 0.15

# Initial condition
Vout0 = [0.0]


# Solve using solve_ivp
nnivp = 500
ts = np.linspace(ta, tb, nnivp)

sol = solve_ivp(fun1, (ta, tb), Vout0, t_eval=ts)

ys = sol.y[0]


# Solve using Euler's method
Ne = 500

tes = np.linspace(ta, tb, Ne)
h = (tb - ta) / (Ne - 1)

yes = np.zeros(Ne)
yes[0] = Vout0[0]

for j in range(Ne - 1):
    tj = tes[j]
    yj = yes[j]

    yes[j+1] = yj + h * fun1(tj, [yj])[0]


# Plot results
plt.figure(figsize=(10, 5))

plt.plot(ts, ys, label="solve_ivp")
plt.plot(tes, yes, "b.", label="Euler")

plt.xlabel("Time (seconds)")
plt.ylabel("Output Voltage (V)")
plt.title(f"Low-pass filter: Euler vs solve_ivp (Ne = {Ne})")

plt.legend()
plt.grid()

plt.show()
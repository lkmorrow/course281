import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Circuit constants
R = 10e3       # Resistance (ohms)
C = 1e-6       # Capacitance (farads)

# Input voltage constants
A = 2.0        # Amplitude (volts)

# Define input voltage function
def Vin(t):
    return A * np.sin(omega * t)


# Define the ODE
def fun1(t, Vout):
    dVoutdt = (Vin(t) - Vout[0]) / (R * C)
    return [dVoutdt]


# Time domain
ta = 0
tmax = 0.15
nn = 500
ts = np.linspace(ta, tmax, nn)

# Initial condition
Vout0 = [0.0]

# Run for both frequencies
for omega in [50, 300]:

    # Calculate input voltage
    vin = Vin(ts)

    # Solve ODE using solve_ivp
    sol = solve_ivp(
        fun1,
        (ta, tmax),
        Vout0,
        t_eval=ts
    )

    vout = sol.y[0]

    # Plot input and output voltage
    plt.figure(figsize=(10, 5))
    plt.plot(ts, vin, label="Vin (input voltage)")
    plt.plot(ts, vout, label="Vout (output voltage)")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Voltage (V)")
    plt.title(f"Low-pass filter with omega = {omega} rad/s")
    plt.legend()
    plt.grid()

plt.show()
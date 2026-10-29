import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# (a) Division of complex numbers
# --------------------------------

z1 = (3 + 4j) / (5 + 6j)

print("(a) Complex number division:")
print("(3 + 4j) / (5 + 6j) =", z1)
print("Real part =", z1.real)
print("Imaginary part =", z1.imag)


# --------------------------------
# (b) Euler's formula
# --------------------------------

print("\n(b) Euler's formula:")

print("exp(2j) =", np.exp(2j))
print("cos(3j) =", np.cos(3j))


# --------------------------------
# (c) Complex exponential function
# --------------------------------

# Set z outside the function
z = 5.0 + 0.2j

# Define f(t) = exp(i*z*t)
def f(t):
    return np.exp(1j * z * t)


# Create an array of time values
t = np.linspace(0, 10, 1000)

# Calculate f(t)
ft = f(t)


# Create one figure with two graphs side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First graph: real and imaginary parts versus t
ax[0].plot(t, ft.real, label='Real part')
ax[0].plot(t, ft.imag, label='Imaginary part')
ax[0].set_xlabel('t')
ax[0].set_ylabel('f(t)')
ax[0].set_title('Real and Imaginary Parts vs t')
ax[0].legend()
ax[0].grid()

# Second graph: imaginary part versus real part
ax[1].plot(ft.real, ft.imag)
ax[1].set_xlabel('Real part')
ax[1].set_ylabel('Imaginary part')
ax[1].set_title('Imaginary Part vs Real Part')
ax[1].set_aspect('equal', adjustable='box')
ax[1].grid()

# Display both graphs in the same window
plt.tight_layout()
plt.show()
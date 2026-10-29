import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-5, 5, 100)

# Plot 1
plt.subplot(3, 2, 1)
plt.plot(x, x)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x")

# Plot 2
plt.subplot(3, 2, 2)
plt.plot(x, x**2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2")

# Plot 3
plt.subplot(3, 2, 3)
plt.plot(x, x**3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^3")

# Plot 4
plt.subplot(3, 2, 4)
plt.plot(x, np.sin(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = sin(x)")

# Plot 5
plt.subplot(3, 2, 5)
plt.plot(x, np.cos(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(x)")

# Plot 6
plt.subplot(3, 2, 6)
plt.plot(x, np.exp(-x**2))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian")

# Add space between the rows of plots
plt.subplots_adjust(hspace=0.5)

# Display all six plots
plt.show()
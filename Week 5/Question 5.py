import numpy as np
import matplotlib.pyplot as plt

# Define the wave function
def psi(x, y):
    r = np.sqrt(x**2 + y**2)
    return x * (6 - r) * np.exp(-r / 3)


# Create x and y values from -20 to 20
x = np.linspace(-20, 20, 200)
y = np.linspace(-20, 20, 200)

# Create a 2D grid
x, y = np.meshgrid(x, y)

# Calculate psi at every point
z = psi(x, y)

# Make a density plot
plt.imshow(z, extent=[-20, 20, -20, 20], origin="lower")

# Label the axes
plt.xlabel("x")
plt.ylabel("y")

# Add a title
plt.title(r"Hydrogen Atom Wave Function $\psi(x,y)$")

# Add a colorbar to show the values of psi
plt.colorbar(label=r"$\psi(x,y)$")

# Show the plot
plt.show()
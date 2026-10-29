import numpy as np
import matplotlib.pyplot as plt

# Define the wave function
def psi(x, y):
    # Calculate r
    r = np.sqrt(x**2 + y**2)

    # Calculate and return the wave function
    return x * (6 - r) * np.exp(-r / 3)


# Create x and y values from -20 to 20
x = np.linspace(-20, 20, 200)
y = np.linspace(-20, 20, 200)

# Create a 2D grid of x and y values
x, y = np.meshgrid(x, y)

# Calculate the wave function at every point
z = psi(x, y)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Make the surface plot
ax.plot_surface(x, y, z, cmap='coolwarm')

# Label the axes
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel(r"$\psi(x,y)$")

# Add a title
ax.set_title("Hydrogen Atom Atomic Orbital")

# Display the plot
plt.show()
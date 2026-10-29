import numpy as np
import matplotlib.pyplot as plt

# Make x and y values
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)

# Make a 2D grid of x and y values
x, y = np.meshgrid(x, y)

# Calculate r
r = np.sqrt(x**2 + y**2)

# Calculate theta using arctan2
theta = np.arctan2(y, x)

# Calculate s(x,y)
s = np.cos(r + theta)

# Make the density plot
plt.imshow(s, extent=[-10, 10, -10, 10], origin="lower")
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$s(x,y)=\cos(r+\theta)$")
plt.colorbar(label="s(x,y)")

'''As you move around the origin and theta changes, the corresponding
value of r also changes. Instead of staying at the same distance from the
origin, the pattern moves inward or outward as you go around, creating a spiral.'''

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define x and y values
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)

# Create a grid
X, Y = np.meshgrid(x, y)

# Calculate r and theta
r = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)


# Calculate w(x, y)
w = np.cos(r + theta / 2)

# Make the density plot
plt.figure()
plt.imshow(w, extent=[-10, 10, -10, 10],
           origin='lower', aspect='equal')

# Add a colour bar and labels
plt.colorbar(label='w(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part (b): w(x, y) = cos(r + theta/2)')

plt.show()

'''The distance causes the cosine to oscillate as you move away from the origin, while the angle
changes the position of the peaks and troughs around the origin. Compared with part (a), the
angle is divided by 2, so it has less influence on the pattern and the spiral winds differently.
The horizontal cutoff occurs because arctan2 has a discontinuity along the negative x-axis,
where the angle jumps from pi to negative pi.'''
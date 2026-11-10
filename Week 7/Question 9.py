import numpy as np
import matplotlib.pyplot as plt

# Create 100 random points
rng = np.random.default_rng()
x = rng.normal(size=100)
y = rng.normal(size=100)

# Choose the rotation angle
theta = np.pi / 2  # Try a very small angle too, e.g. 0.01.
# 0.01 makes the two colors become very close to each other,
# due to a very small rotation

# Rotate the points
xr = x * np.cos(theta) - y * np.sin(theta)
yr = x * np.sin(theta) + y * np.cos(theta)

# Plot the original and rotated points
plt.plot(x, y, 'bo', label='Original points')
plt.plot(xr, yr, 'ro', label='Rotated points')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Original and rotated points')
plt.axis('equal')
plt.legend()
plt.show()
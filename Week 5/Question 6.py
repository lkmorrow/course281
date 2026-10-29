import numpy as np
import matplotlib.pyplot as plt

# Set the radius of the sphere
r = 5

# Set the number of points in each angle direction
nn = 20

# Create empty lists to store the coordinates
xlist = []
ylist = []
zlist = []

# Go through values of theta from 0 to pi
for theta in np.linspace(0, np.pi, nn):

    # Go through values of phi from 0 to 2*pi
    for phi in np.linspace(0, 2 * np.pi, nn):

        # Convert spherical coordinates to Cartesian coordinates
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        # Add each coordinate to its list
        xlist.append(x)
        ylist.append(y)
        zlist.append(z)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot all the points
ax.scatter(xlist, ylist, zlist)

# Label the axes and add a title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_aspect('equal')
ax.set_title("Points on a Sphere")

# Display the plot
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define the Particle class from the notes
class Particle:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

# Set the number of particles and the radius
N = 50
R = 10

# Create an empty list for the particles
cparts = []

# Calculate the position of each particle
for theta in np.linspace(0, 2 * np.pi, N, endpoint=False):

    x = R * np.cos(theta)
    y = R * np.sin(theta)

    cparts.append(Particle(x, y))

# Plot the particle positions
for p in cparts:
    plt.plot(p.x, p.y, 'mo')

plt.xlabel('x')
plt.ylabel('y')
plt.title('50 Particles on a Circle')

# Set the aspect ratio so the circle looks circular
ax = plt.gca()
ax.axis('equal')

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define the Particle class from the notes
class Particle:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

# Make particles in the ring between radius 3 and radius 5
cparts = []

for x in np.linspace(-5, 5, 40):
    for y in np.linspace(-5, 5, 40):

        # Calculate the distance from the origin
        r = np.sqrt(x**2 + y**2)

        # Only create particles inside the ring
        if r > 3 and r < 5:
            cparts.append(Particle(x, y))

# Plot the particle positions
for p in cparts:
    plt.plot(p.x, p.y, 'mo')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Particles in a Ring')

# Make the x and y axes have the same scale
ax = plt.gca()
ax.axis('equal')

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Make 20 x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 20)

# Calculate the two functions
f1 = np.sin(x)
f2 = np.cos(x)

# Set the overall font size
plt.rcParams.update({'font.size': 14})

# Plot the two functions
plt.plot(x, f1, 'o-', label=r'$\sin(x)$')
plt.plot(x, f2, 's--', label=r'$\cos(x)$')

# Label the x-axis using the Greek letter theta
plt.xlabel(r'$\theta$ (radians)')

# Label the y-axis
plt.ylabel(r'$\sin(\theta),\ \cos(\theta)$', fontsize=16)

# Add a title containing a mathematical formula
plt.title(r'Functions for $\sin(\theta)$ and $\cos(\theta)$', fontsize=18)

# Add the legend
plt.legend(fontsize=12)

# Set the y-axis limits
plt.ylim(-1.5, 1.5)
plt.grid(True)

# Show the graph
plt.show()
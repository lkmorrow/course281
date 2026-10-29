import numpy as np
import matplotlib.pyplot as plt

# Create 200 x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 200)

# Print the x array to make sure it worked
print("x values:")
print(x)

# Calculate the first function for every x value
f1 = np.sin(x)

# Calculate the second function for every x value
f2 = np.cos(x)

# Print the function values
print("f1 values:")
print(f1)

print("f2 values:")
print(f2)

# Plot f1 by itself
plt.plot(x, f1)
plt.xlabel("x")
plt.ylabel("f1(x)")
plt.title("f1(x) = sin(x)")
plt.ylim(-1.5, 1.5)
# plt.show()

# Plot f2 by itself
plt.plot(x, f2)
plt.xlabel("x")
plt.ylabel("f2(x)")
plt.title("f2(x) = cos(x)")
plt.ylim(-1.5, 1.5)
# plt.show()

# Plot both functions on the same graph
# 'b-' means blue solid line
# 'r--' means red dashed line
plt.plot(x, f1, 'b-', label="sin(x)")
plt.plot(x, f2, 'r--', label="cos(x)")

# Add labels and a title
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x) and cos(x)")

# Force the y-axis to go from -1.5 to 1.5
plt.ylim(-1.5, 1.5)

# Show a legend identifying the two lines
plt.legend()

# Display the graph
plt.show()
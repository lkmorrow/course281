import numpy as np

# Create the two matrices
A = np.array([[1, 3],
              [2, 4],
              [5, 6]])

B = np.array([[2, 1, 4],
              [3, 2, 1]])

# Print the matrices
print('A =\n', A)
print('B =\n', B)

# Calculate and print the matrix products
print('A @ B =\n', A @ B)
print('B @ A =\n', B @ A)

"""The matrix products calculated by NumPy agree with the hand calculations.
Notice that AB and BA are different, showing that matrix multiplication
is generally not commutative: AB != BA."""
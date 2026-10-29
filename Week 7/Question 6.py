import numpy as np

# Create matrix C
C = np.array([[1, 3, 2],
              [2, 4, 1],
              [5, 6, 5]])

# Calculate the inverse
Cinv = np.linalg.inv(C)

# Print the matrices
print('C =\n', C)
print('C inverse =\n', Cinv)
print('C inverse @ C =\n', Cinv @ C)

"""Yes, this is the result we expect.
The product C^-1 C is approximately the identity matrix, as expected.
This confirms that the inverse of C, calculated using Python, is correct,
allowing for small numerical rounding errors."""
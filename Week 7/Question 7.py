import numpy as np

# Matrix of coefficients
A = np.array([[1,  4,  1],
              [4, -1, -1],
              [2,  1,  3]])

# Right-hand-side vector
b = np.array([-4, 3, 7])

# Method (a): Multiply the inverse of A by b
solution1 = np.linalg.inv(A) @ b

# Method (b): Solve the equations directly
solution2 = np.linalg.solve(A, b)

# Print both solutions
print('Solution using inverse =', solution1)
print('Solution using linalg.solve =', solution2)

# Check whether both methods agree
print('Do the solutions agree?', np.allclose(solution1, solution2))

# Check the solution in the first original equation
x, y, z = solution2
print('Check first equation:', x + 4*y + z)
print('Expected result: -4')
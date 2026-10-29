import numpy as np

# Try a few different angles in radians
angles = [0, np.pi/4, np.pi/2, np.pi]

for theta in angles:
    # Create the rotation matrix
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])

    # Calculate the transpose times the matrix
    result = R.T @ R

    print('theta =', theta)
    print(result)
    print()

# b. Rotate the point {r}=[1,0]

# Original point
r = np.array([1, 0])

# Angles to test
angles = [np.pi/4, np.pi/2, 3*np.pi/2]

for theta in angles:
    # Create the rotation matrix
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])

    # Rotate the point
    r_new = R @ r

    print('theta =', theta)
    print('Rotated point =', r_new)
    print()
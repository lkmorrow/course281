import numpy as np

# Ask the user how many rows and columns they want
# rr means number of rows, cc means number of columns
rr = int(input("How many rows? "))
cc = int(input("How many columnss? "))

# Create an array aa with rr rows and cc columns
# np.zeros fills the array with zeros at first
aa = np.zeros((rr, cc), int)

# Fill the array with numbers from 1 up to rows * columns
for r in range(rr):
    for c in range(cc):
        # r is the row number and c is the column number
        # Python starts counting at 0, so we add 1
        aa[r, c] = r * cc + c + 1

# Print the entire array
print("Array:\n", aa)

# Print the third column
# : means "all rows"
# 2 means the third column because counting starts at 0
print("Third column:", aa[:, 2])

# Print the fifth row
# 4 means the fifth row because counting starts at 0
# : means "all columns"
print("Fifth row:", aa[4, :])

# Print the upper-left 3 by 3 section
# :3 means the first 3 rows/columns
print("Upper left:\n", aa[:3, :3])

# Print the upper-right 3 by 3 section
# :3 means the first 3 rows
# -3: means the last 3 columns
print("Upper right:\n", aa[:3, -3:])

# Print the transpose of the array
# .T switches the rows and columns
print("Transpose:\n", aa.T)
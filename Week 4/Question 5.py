import numpy as np

# Ask the user for the number of rows and columns
rr = int(input("How many rows? "))
cc = int(input("How many columns? "))

# Create an array filled with zeros
aa = np.zeros((rr, cc), int)

# Fill the array with numbers from 1 to rows * columns
for r in range(rr):
    for c in range(cc):
        aa[r, c] = r * cc + c + 1

# Print the array on the screen
print("Array:\n", aa)

# Save the array to a text file called array.txt
# By default, np.savetxt() saves the numbers as floats
np.savetxt("/Users/liammorrow/course281/Week 4/array.txt", aa)
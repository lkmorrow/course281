import numpy as np

# Ask the user for the number of rows and columns
rr = int(input("rows? "))
cc = int(input("cols? "))

# Create an array filled with zeros
aa = np.zeros((rr, cc), int)

# Fill the array with numbers from 1 to rows * columns
for r in range(rr):
    for c in range(cc):
        aa[r, c] = r * cc + c + 1

# Print the array
print("Array:\n", aa)

# Create column headings
headings = ",".join(["Column " + str(c + 1) for c in range(cc)])

# Save as a CSV file
# %.6f = 6 digits after the decimal point
# delimiter="," = separate values with commas
# header=headings = add column headings
# comments="" = don't put # before the headings
np.savetxt("/Users/liammorrow/course281/Week 4/array.csv", aa, fmt="%.6f", delimiter=",", header=headings, comments="")

print("Array saved to array.csv")
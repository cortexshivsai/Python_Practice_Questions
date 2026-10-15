"""
    *
   ***
  *****
 *******
*********
"""
rows = 5

for i in range(1, rows + 1):

    # Print spaces before the stars
    for j in range(rows - i):
        print(" ", end="")

    # Print an odd number of stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()
"""
*********
 *******
  *****
   ***
    *
"""
rows = 5

for i in range(rows, 0, -1):

    # Print spaces before the stars
    for j in range(rows - i):
        print(" ", end="")

    # Print decreasing odd numbers of stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()
"""
In Pascal's triangle, the first and last numbers of every row are 1. Each number between them is the sum of the two numbers directly above it.
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
"""
from math import comb

rows = 5

for i in range(rows):

    # Print spaces to center the triangle
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print the values in the current row
    for j in range(i + 1):
        print(comb(i, j), end=" ")

    print()
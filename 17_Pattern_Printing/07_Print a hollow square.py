"""
*****
*   *
*   *
*   *
*****
"""
size = 5

for i in range(size):

    for j in range(size):

        # Print stars on the boundary
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            # Print spaces inside the square
            print(" ", end="")

    print()
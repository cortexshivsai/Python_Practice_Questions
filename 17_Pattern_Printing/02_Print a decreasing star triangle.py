"""
*****
****
***
**
*
"""
rows = 5

# Start with 5 stars and decrease each row
for i in range(rows, 0, -1):

    # Print i stars
    for j in range(i):
        print("*", end="")

    # Move to the next line
    print()
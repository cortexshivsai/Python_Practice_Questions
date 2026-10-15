"""
1
12
123
1234
"""

rows = 4

for i in range(1, rows + 1):

    # Print numbers from 1 to the current row number
    for j in range(1, i + 1):
        print(j, end="")

    print()
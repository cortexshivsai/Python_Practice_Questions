"""
Floyd's triangle prints consecutive numbers, starting from 1.
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
rows = 5

# Start counting from 1
number = 1

for i in range(1, rows + 1):

    # Print as many numbers as the current row
    for j in range(i):
        print(number, end=" ")

        # Increase the number after printing
        number += 1

    print()
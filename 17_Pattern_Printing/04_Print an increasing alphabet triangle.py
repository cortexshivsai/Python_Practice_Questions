"""
A
AB
ABC
ABCD
"""
rows = 4

for i in range(1, rows + 1):

    # Print letters from A up to the current row
    for j in range(i):
        letter = chr(65 + j)  # 65 is the ASCII value of A
        print(letter, end="")

    print()
#Convert a binary string to decimal without using int(value, 2).
binary = input("Enter a binary number: ")

decimal = 0
valid = len(binary) > 0

for digit in binary:
    if digit not in "01":
        valid = False
        break

    decimal = decimal * 2 + int(digit)

if valid:
    print("Decimal:", decimal)
else:
    print("Invalid binary number")
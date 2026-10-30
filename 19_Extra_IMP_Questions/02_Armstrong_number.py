#An Armstrong number equals the sum of its digits, each raised to the power of the number of digits. Example: 153 = 1³ + 5³ + 3³.
n = int(input("Enter a number: "))

digits = str(n)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if n >= 0 and total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong") 
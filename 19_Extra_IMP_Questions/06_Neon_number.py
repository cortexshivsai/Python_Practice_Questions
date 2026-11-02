#A Neon number equals the sum of the digits of its square. Example: 9² = 81, and 8 + 1 = 9.
n = int(input("Enter a number: "))

square = n ** 2
total = 0

for digit in str(square):
    total += int(digit)

if n >= 0 and total == n:
    print("Neon Number")
else:
    print("Not Neon")
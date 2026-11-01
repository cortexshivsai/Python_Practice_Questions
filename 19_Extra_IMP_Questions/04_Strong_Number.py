#A Strong number equals the sum of the factorials of its digits. Example: 145 = 1! + 4! + 5!.
import math

n = int(input("Enter a number: "))
total = 0

for digit in str(n):
    total += math.factorial(int(digit))

if n >= 0 and total == n:
    print("Strong Number")
else:
    print("Not Strong")
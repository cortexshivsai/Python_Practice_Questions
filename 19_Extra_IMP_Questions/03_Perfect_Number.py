#A perfect number equals the sum of its positive divisors excluding itself. Example: 6 = 1 + 2 + 3.
n = int(input("Enter a number: "))

total = 0

for i in range(1, n):
    if n > 0 and n % i == 0:
        total += i

if n > 0 and total == n:
    print("Perfect Number")
else:
    print("Not Perfect")
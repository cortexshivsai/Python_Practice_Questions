#A Spy number has equal digit sum and digit product. Example: 1124 has sum 8 and product 8.
n = int(input("Enter a number: "))

digits = str(n)
total = 0
product = 1

for digit in digits:
    d = int(digit)
    total += d
    product *= d

if n >= 0 and total == product:
    print("Spy Number")
else:
    print("Not Spy")
#The GCD is the largest number that divides both numbers exactly. Example: GCD of 12 and 18 is 6.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD:", a)
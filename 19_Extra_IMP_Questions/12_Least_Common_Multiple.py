#The LCM is the smallest positive number divisible by both numbers.
a = int(input("Enter first positive number: "))
b = int(input("Enter second positive number: "))

if a <= 0 or b <= 0:
    print("Enter positive numbers")
else:
    x = a
    y = b

    while y != 0:
        x, y = y, x % y

    gcd = x
    lcm = (a * b) // gcd

    print("LCM:", lcm)
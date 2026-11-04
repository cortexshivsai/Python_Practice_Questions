#For this challenge, a Magic number is one whose digits can repeatedly be summed until the result is 1. Example: 19 → 1 + 9 = 10 → 1 + 0 = 1.
n = int(input("Enter a number: "))

if n <= 0:
    print("Not a Magic Number")
else:
    while n > 9:
        total = 0

        for digit in str(n):
            total += int(digit)

        n = total

    if n == 1:
        print("Magic Number")
    else:
        print("Not a Magic Number")
#A number is happy if repeatedly summing the squares of its digits eventually reaches 1. Example: 19 → 82 → 68 → 100 → 1.
n = int(input("Enter a number: "))
num = n
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    total = 0

    for digit in str(num):
        total += int(digit) ** 2

    num = total

if n > 0 and num == 1:
    print("Happy Number")
else:
    print("Not Happy")
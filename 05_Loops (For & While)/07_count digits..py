#Count digits.
num = int(input("Enter a number: "))
original_num = num
count = 0
if num == 0:
    count = 1
else:
    while num > 0:  # Loop until the number becomes 0
        count += 1        # Increase digit count
        num = num // 10   # Remove the last digit
print(f"Number of digits in {original_num} is {count}")

#using for loop
'''num = input("Enter a number: ")
count = 0

for digit in num:
    count += 1

print("Number of digits:", count)'''
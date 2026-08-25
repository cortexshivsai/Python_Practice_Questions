#Find greatest among three numbers using operators.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is:", a)
elif b >= a and b >= c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)




# a = 10
# b = 25
# c = 40

# greatest_ab = (a + b + abs(a - b)) // 2

# greatest = (greatest_ab + c + abs(greatest_ab - c)) // 2

# print(greatest)
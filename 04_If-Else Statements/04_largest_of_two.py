#Find largest of two numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print(f"The First Number {num1} is Largest")
elif num1==num2:
    print(f"Both Numbers {num1} and {num2} are Equal")  
else:
    print(f"The Second Number {num2} is Largest")      
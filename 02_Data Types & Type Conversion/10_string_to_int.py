#Take input as string and convert it into integer before addition.
num1=input("Enter first number:")
num2=input("Enter second number:")
print("Before Conversion: ")
sum=num1+num2
print(f"The Sum of strings is: {sum} and its type is {type(sum)}")
print("After Conversion: ")
sum1=int(num1)+int(num2)
print(f"Sum of the two numbers is {sum1} and its type is {type(sum1)}")
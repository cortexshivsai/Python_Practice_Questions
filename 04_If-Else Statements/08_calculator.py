num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
cal=input("Enter What you want to perform between +,-,* & /: ")
if cal=="+":
    print(f"Addition is: {num1+num2}")
elif cal=="-":
    print(f"Subtraction is: {num1-num2}") 
elif cal=="*" :
    print(f"Multiplication is: {num1*num2}") 
elif cal=="/":
    print(f"Division is: {num1/num2}")
else:
    print("Enter Valid Action")           
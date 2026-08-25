#Find largest of three numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
# if num1>num2 and num1>num3:
#     print(f"The First Number {num1} is Largest")
# elif num2>num1 and num2>num3:
#     print(f"The second number {num2} is largest") 
# elif num1==num2==num3:
#     print(f"All the three numbers are Equal")     
# elif num3>num1 and num3>num2:
#     print(f"The Third Number {num3} is Largest")   
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2    
elif num3>num1 and num3>num2:
    largest=num3
else:
    largest="All three numbers are equal"
    print(largest)
    pass
if(num1==largest or num2==largest or num3==largest):
    print(f"Number {largest} is largest")            


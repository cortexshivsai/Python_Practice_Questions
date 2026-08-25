#Check divisible by both 5 and 11.
num=int(input("Enter any number: "))
if num%5==0 and num%11==0:
    print(f"Number {num} is divisible by both 5 and 11")
else:
    print(f"Number {num} is not divisible by both 5 and 11")

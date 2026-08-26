#Palindrome number
num = int(input("Enter a number: "))
og=num

reverse = 0 
while num>0:
    digit = num % 10     # Extract the last digit of the number
    reverse = reverse * 10 + digit 
    num=num//10    # Add the extracted digit to the reversed number 
if og==reverse:
    print(f"The Number {og} is a palindrome number") 
else:
    print(f"The number {og} is not a palindrome number")       
#Reverse a number.
num = int(input("Enter a number: "))

reverse = 0 # Variable to store the reversed number

while num > 0:
    digit = num % 10     # Extract the last digit of the number
    reverse = reverse * 10 + digit     # Add the extracted digit to the reversed number
    num = num // 10     # Remove the last digit from the original number

print("Reversed number:", reverse)
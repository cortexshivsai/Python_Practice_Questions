#Handle Invalid Input
try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input. Please enter a number.")
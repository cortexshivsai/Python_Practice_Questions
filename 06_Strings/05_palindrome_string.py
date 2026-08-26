#Check palindrome string.
string = input("Enter a string: ")

reverse =""

for char in string:
    reverse = char + reverse


if string==reverse:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")


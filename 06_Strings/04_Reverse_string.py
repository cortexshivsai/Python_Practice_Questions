#Reverse a string. method 1
# str1=input("Enter any string:")
# print(str1[::-1])

#Method 2
string = input("Enter a string: ")

reverse =""

for char in string:
    reverse = char + reverse

print("Reversed String:", reverse)
#Count occurrence of a character.
#Method1
string = input("Enter a string: ")
ch = input("Enter the character to count: ")
count = 0
for char in string:
    if char == ch:
        count += 1
print(f"'{ch}' occurs {count} times.")


#Method2
# string = input("Enter a string: ")
# ch = input("Enter the character to count: ")

# print(f"'{ch}' occurs {string.count(ch)} times.")
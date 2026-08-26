#Find frequency of every character.
string = input("Enter a string: ")

frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character Frequencies:")
for char in frequency:
    print(char, ":", frequency[char])

#Method 2
# string = input("Enter a string: ")

# for char in string:
#     if string.count(char) > 0:
#         print(char, ":", string.count(char))    
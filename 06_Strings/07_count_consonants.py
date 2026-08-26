#Count consonants.
string = input("Enter a string: ")
count = 0
string = string.lower()
for char in string:
    if  char not in "aeiouAEIOU":
        count += 1

print("Number of consonants:", count)
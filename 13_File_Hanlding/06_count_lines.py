#Count Lines
# Method 1
with open("data.txt", "r") as file:
    lines = file.readlines()# readlines() counts the number of lines in the file

print("Number of lines:", len(lines))

# Method 2
# file = open("data.txt", "r")
# lines = file.readlines()
# print("Number of lines:", len(lines))
# file.close()
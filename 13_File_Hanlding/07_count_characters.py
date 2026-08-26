#Count characters
# Method 1
with open("data.txt", "r") as file:
    data = file.read()

print("Number of characters:", len(data))


# Method 2
# file = open("data.txt", "r")
# data = file.read() #This counts characters present in the file with the spaces and newline characters.
# print("Number of characters:", len(data))
# file.close()
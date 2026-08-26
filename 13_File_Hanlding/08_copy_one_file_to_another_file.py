#Copy one file to another file
# Method 1
with open("data.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully")



# Method 2
# source = open("data.txt", "r")
# data = source.read()
# source.close()
# destination = open("copy.txt", "w")
# destination.write(data)
# destination.close()
# print("File copied successfully")
#Read file
#Method 1
with open("data.txt", "r") as file:#"r" means read mode
    data = file.read()

print(data)


# Method 2
# file = open("data.txt", "r")
# data = file.read()
# print(data)
# file.close()
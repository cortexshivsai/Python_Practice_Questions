#replace one word with another
# Method 1
with open("data.txt", "r") as file:
    data = file.read()

data = data.replace("Python", "Java")

with open("data.txt", "w") as file:
    file.write(data)

print("Word replaced successfully")


# Method 2
# file = open("data.txt", "r")
# data = file.read()
# file.close()
# data = data.replace("Python", "Java")
# file = open("data.txt", "w")
# file.write(data)
# file.close()
# print("Word replaced successfully")
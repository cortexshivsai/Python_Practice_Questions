#Write into file
#Method 1
with open("data.txt", "w") as file:#"w" means write mode. It will overwrite existing content.
    file.write("Hello Python")

print("Data written successfully")


#Method 2
# file = open("data.txt", "w")
# file.write("Hello I am Shivsai")
# file.close()
# print("Data written successfully")
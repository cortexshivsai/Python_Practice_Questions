#Append Data
#Method 1
with open("data.txt", "a") as file:#"a" adds new data at the end without deleting existing content.
    file.write("\nWelcome to Python")

print("Data appended successfully")


#Method 2
# file = open("data.txt", "a")
# file.write("\nI am learning Python")
# file.close()
# print("Data appended successfully")
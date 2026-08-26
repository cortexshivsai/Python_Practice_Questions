#Count Words
# Method 1
with open("data.txt", "r") as file:
    data = file.read()

words = data.split()#split() separates the text into words.

print("Number of words:", len(words))


# Method 2
# file = open("data.txt", "r")
# data = file.read()
# words = data.split()
# print("Number of words:", len(words))
# file.close()
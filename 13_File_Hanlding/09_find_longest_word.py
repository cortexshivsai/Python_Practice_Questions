#Find longest word
#Method 1
with open("data.txt", "r") as file:
    data = file.read()

words = data.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


#Method 2
# file = open("data.txt", "r")
# data = file.read()
# words = data.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest word:", longest)
# file.close()
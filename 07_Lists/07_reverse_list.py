#Reverse list.
#Method 1
# chars = list( input("Enter characters separated by spaces: ").split())

# print("Reversed List:", chars[::-1])
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# print("Reversed List:", numbers[::-1])

#Method 2
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# numbers.reverse()

# print("Reversed List:", numbers)

#Method 3
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])
print("Reversed List:", reverse)

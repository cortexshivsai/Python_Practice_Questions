#Remove duplicates.
#Method 1
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# unique = []
# for num in numbers:

#     if num not in unique:
#         unique.append(num)
# print("List after removing duplicates:", unique)

#Method 2
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers = list(set(numbers))

print("List after removing duplicates:", numbers)
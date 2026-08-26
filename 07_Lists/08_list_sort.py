#Sort a list
#Method 1
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# numbers.sort()
# print("Sorted List: ",numbers)
#Method 2
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_list = sorted(numbers)

print("Sorted List:", sorted_list)

#Method 3
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# # Bubble Sort
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted List:", numbers)
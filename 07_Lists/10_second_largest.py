#Find second largest element.
#Method 1
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# for num in numbers:
#     if num > second_largest and num != largest:
#         second_largest = num
# print("Second Largest Element:", second_largest)

#Method 2
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# numbers.sort()

# print("Second Largest Element:", numbers[-2])

#Method 3
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
numbers.remove(largest)

print("Second Largest Element:", max(numbers))
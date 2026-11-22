numbers = [5, 2, 8, 1, 3]

n = len(numbers)

for i in range(n):
    min_index = i

    # Find the smallest element in the remaining list
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Place the smallest element at the current position
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)
numbers = [5, 2, 8, 1, 3]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):

        # Swap adjacent elements if they are in the wrong order
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
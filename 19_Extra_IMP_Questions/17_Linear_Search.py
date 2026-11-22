numbers = [10, 25, 30, 45, 50]
target = int(input("Enter the number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
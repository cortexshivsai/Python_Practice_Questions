n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")

    # Calculate the next Fibonacci number
    c = a + b
    a = b
    b = c
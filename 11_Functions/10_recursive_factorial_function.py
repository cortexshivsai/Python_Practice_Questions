#Recursive factorial function
def factorial(num):

    # Base case
    if num == 0 or num == 1:
        return 1

    # Recursive call
    return num * factorial(num - 1)


print("Factorial:", factorial(5))
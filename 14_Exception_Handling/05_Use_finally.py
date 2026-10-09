#05_Use_finally
try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input")

finally:
    print("Program completed")
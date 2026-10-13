# Import our own calculator module
import calculator

# Call functions from the module
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))


#07_Import a Specific Function

# Import only the add() function
from calculator import add

# Call the function directly
result = add(20, 30)

print("Sum:", result)
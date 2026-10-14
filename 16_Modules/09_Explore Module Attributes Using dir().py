#Explore Module Attributes Using dir()
# Import the math module
import math

# Display the names available in the math module
print(dir(math))

# Check whether sqrt is available
print("sqrt" in dir(math))

# Check whether factorial is available
print("factorial" in dir(math))

# Display the value of pi
print("Value of pi:", math.pi)
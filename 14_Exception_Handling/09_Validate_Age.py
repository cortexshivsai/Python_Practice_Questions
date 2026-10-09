#Validate Age
try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Invalid age")

    print("Valid age:", age)

except ValueError as e:
    print(e)




# try:
#     age = int(input("Enter your age: "))

#     if age < 0 or age > 120:
#         raise ValueError("Age must be between 0 and 120")

#     print("Valid age:", age)

# except ValueError:
#     print("Please enter a valid age between 0 and 120")
    
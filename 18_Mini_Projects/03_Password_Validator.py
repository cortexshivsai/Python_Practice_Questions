print("=== Password Validator ===")

password = input("Enter a password: ")

# Flags to track the password requirements
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

# Check all requirements together
if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("Minimum length: 8 characters")
    print("Include uppercase, lowercase, digit, and special character.")
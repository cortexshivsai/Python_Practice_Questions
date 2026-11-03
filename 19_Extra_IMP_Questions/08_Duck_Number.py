#A Duck number contains at least one zero, but not as a leading zero. Example: 1023 is a Duck number.
n = input("Enter a positive integer: ")

if n.isdigit() and n[0] != "0" and "0" in n:
    print("Duck Number")
else:
    print("Not Duck")
#An Automorphic number's square ends with the original number. Example: 25² = 625.
n = int(input("Enter a number: "))

square = n ** 2

if n >= 0 and str(square).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not Automorphic")
#Predict outputs of complex operator expressions.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))  


print("1. Arithmatic Operators: ")
print("1.", a + b * 2)
print("2.", (a + b) * 2)
print("3.", a / b)
print("4.", a // b)
print("5.", a % b)
print("6.", a ** 2)

print("2. Comparison Operators: ")
print("7.", a > b)
print("8.", a < b)
print("9.", a == b)
print("10.", a != b)

print("3. Logical Operators: ")
print("11.", a > b and b > c)
print("12.", a < b or b > c)
print("13.", not(a > b))

print("4. Truthy/Falsy with and / or: ")
print("14.", a and b)
print("15.", c and b)
print("16.", a or c)#
print("17.", c or b)

print("5. Bitwise Operators: ")
print("18.", a & b)
print("19.", a | b)
print("20.", a ^ b)
print("21.", a << 1)
print("22.", a >> 1)

print("6. Boolean and Truth Value: ")
print("23.", True + False)
print("24.", bool(""))
print("25.", bool("Python"))
print("26.", bool([]))
print("27.", bool([1, 2]))

print("7. Mixed / Complex Expressions:  ")
print("28.", a > c == True)
print("29.", a + b > 10 and a - b < 10)
print("30.", (b + c) % 2 == 0)
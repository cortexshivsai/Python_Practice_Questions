#Function using *args
def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))
#*args    → multiple positional arguments → tuple
#Find maximum using lambda
from functools import reduce
numbers = [10, 25, 15, 40, 30]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)
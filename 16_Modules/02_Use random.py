# Use Random
# Import the random module
import random

# Generate a random integer between 1 and 100
number = random.randint(1, 100)

print("Random number:", number)

# Select a random item from a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruit = random.choice(fruits)

print("Random fruit:", fruit)

# Shuffle the elements of a list
numbers = [10, 20, 30, 40, 50]

random.shuffle(numbers)

print("Shuffled list:", numbers)

# Generate a random decimal between 0.0 and 1.0
decimal = random.random()

print("Random decimal:", decimal)

"""

Example output :
Random number: 47
Random fruit: Mango
Shuffled list: [30, 50, 10, 40, 20]
Random decimal: 0.6382


Function                                     Purpose

random.randint(1, 100)             Random integer from 1 to 100, inclusive

random.choice(list)                  Selects one random item

random.shuffle(list)                 Shuffles a list in place

random.random()                     Random decimal from 0.0 up to, but not including, 1.0

"""
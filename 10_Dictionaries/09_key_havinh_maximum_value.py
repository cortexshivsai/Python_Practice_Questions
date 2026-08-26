marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 88
}

maximum = 0
max_key = ""

for key in marks:
    if marks[key] > maximum:
        maximum = marks[key]
        max_key = key

print("Highest marks:", max_key)
print("Marks:", maximum)
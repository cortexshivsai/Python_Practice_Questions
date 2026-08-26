#Soet tuple using second element
students = [
    ("Rahul", 85),
    ("Amit", 70),
    ("Sneha", 95),
    ("Priya", 80)
]
students.sort(key=lambda x: x[1])
print(students)
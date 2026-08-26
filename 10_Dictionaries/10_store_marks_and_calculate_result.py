marks = {
    "Math": 80,
    "English": 70,
    "Science": 90,
    "Computer": 85
}

total = 0

for mark in marks.values():
    total += mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
def calculate_result(marks):
    total = 0

    # Add all subject marks
    for mark in marks.values():
        total += mark

    average = total / len(marks)

    # Every subject must have at least 35 marks
    passed = all(mark >= 35 for mark in marks.values())

    print("\n=== Student Result ===")
    print("Subject-wise Marks:")

    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("Total:", total)
    print(f"Average: {average:.2f}")

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")


student_name = input("Enter student name: ")

marks = {}

# Collect marks for three subjects
for subject in ["Python", "Maths", "English"]:
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= mark <= 100:
                marks[subject] = mark
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Enter a whole number.")

print("\nStudent:", student_name)
calculate_result(marks)
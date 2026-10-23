questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. C#", "D. Ruby"],
        "answer": "B"
    },
    {
        "question": "Which keyword defines a function?",
        "options": ["A. func", "B. function", "C. def", "D. define"],
        "answer": "C"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    }
]

score = 0

print("=== Python Quiz ===")

# Ask every question
for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer not in ["A", "B", "C", "D"]:
        print("Invalid option. No point awarded.")
    elif answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", question["answer"])

print("\n=== Quiz Result ===")
print("Your score:", score, "out of", len(questions))
print(f"Percentage: {score / len(questions) * 100:.2f}%")
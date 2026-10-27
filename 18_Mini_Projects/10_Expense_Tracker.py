expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        category = input("Enter category: ").strip()

        try:
            amount = float(input("Enter amount (₹): "))

            if not category:
                print("Category cannot be empty.")
            elif amount <= 0:
                print("Amount must be greater than zero.")
            else:
                # Store each expense as a dictionary
                expense = {
                    "category": category,
                    "amount": amount
                }

                expenses.append(expense)
                print("Expense added successfully.")

        except ValueError:
            print("Enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nRecorded Expenses:")

            for number, expense in enumerate(expenses, start=1):
                print(
                    f"{number}. {expense['category']}: "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = 0

        # Add the amount from every expense
        for expense in expenses:
            total += expense["amount"]

        print(f"Total expenses: ₹{total:.2f}")

    elif choice == "4":
        print("Expense Tracker closed.")
        break

    else:
        print("Invalid choice.")
def show_menu():
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


balance = 5000.0

while True:
    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print(f"Available balance: ₹{balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                balance += amount
                print(f"Deposit successful. Balance: ₹{balance:.2f}")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrawal successful. Balance: ₹{balance:.2f}")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid menu choice. Try again.")
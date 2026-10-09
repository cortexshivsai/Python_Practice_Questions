#ATM Withdrawal Exception
class InsufficientBalanceError(Exception):
    pass


balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as e:
    print(e)

except InsufficientBalanceError as e:
    print(e)

finally:
    print("Thank you for using the ATM")
# Encapsulation :Encapsulation means keeping data and the methods that operate on that data together inside a class.
# It is also commonly used to restrict direct access to data.
#In Python, we can use __ to make a variable private-like.

class BankAccount:

    def __init__(self, balance):
        # Private variable
        self.__balance = balance

    # Method to check balance
    def show_balance(self):
        print("Current balance:", self.__balance)

    # Method to deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Money deposited successfully")
        else:
            print("Invalid amount")


# Creating object
account = BankAccount(5000)

# Accessing balance through a method
account.show_balance()

# Depositing money
account.deposit(2000)

# Checking balance again
account.show_balance()


"""self.__balance

is private-like.

We access it through methods:

show_balance()
deposit()

This gives us better control over the data.

Simple meaning:
Encapsulation = Keep data + methods together
                 and control how the data is accessed."""
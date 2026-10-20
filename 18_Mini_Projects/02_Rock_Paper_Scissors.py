import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors ===")
print("Choose: rock, paper, or scissors")

user = input("Your choice: ").strip().lower()

# Computer selects a random choice
computer = random.choice(choices)

print("Your choice:", user)
print("Computer's choice:", computer)

if user not in choices:
    print("Invalid choice! Please try again.")

elif user == computer:
    print("It's a draw!")

elif (
    (user == "rock" and computer == "scissors")
    or (user == "paper" and computer == "rock")
    or (user == "scissors" and computer == "paper")
):
    print("You win!")

else:
    print("Computer wins!")
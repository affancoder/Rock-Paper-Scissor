import random
print("Rock Paper Scissors Game\n")
user_choice = int(input("Type 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n\nEnter your Choice: "))
if user_choice == 0:
    print("\nYou have chosen Rock 👍🏻\n")
elif user_choice == 1:
    print("You have chosen Paper📰\n")
elif user_choice == 2:
    print("You have chosen Scissors ✂️\n")
else:
    print("invalid operation 😑")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("computer has chosen Rock 👍🏻\n")
elif computer_choice == 1:
    print("computer has chosen Paper\n")
else:
    print("computer has chosen Scissors ✂️\n")

if computer_choice == user_choice:
    print("It's a draw match")

elif computer_choice == 0 and user_choice == 1:
    print("You win the match")
elif computer_choice == 0 and user_choice == 2:
    print("You lose the game")
elif computer_choice == 1 and user_choice == 0:
    print("You win the match")
elif computer_choice == 1 and user_choice == 2:
    print("You win the match")
elif computer_choice == 2 and user_choice == 1:
    print("You lose the game")
elif computer_choice == 2 and user_choice == 0:
    print("You win the match")
else:
    print("invalid operation 😑")

# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

#print(user_choice)
print("USER CHOICE:", user_choice)

# validate the input such that only if it is one of the expected values
# ... will we continue with the rest of the program
# ...otherwise we'll stop the program before it tries to do anything else
# ...and we'll ask the user to run the program again

# and
# or 

# if user_choice = "rock" or "paper" or "scissors":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid. Keep going.")
else:
    print("OOPS. Invalid input. Please try again.")
    exit()


valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock beats scissors! You lose.")

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")
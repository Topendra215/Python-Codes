import random
print("Welcome to the Rock paper scissor game")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# Get the user's choice
user_choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))

# Check if the user's input is valid before proceeding
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number. Please enter a number between 0 and 2.")
else:
    print("You chose:")
    print(game[user_choice])

    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game[computer_choice])

    # Determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("It's a draw!")



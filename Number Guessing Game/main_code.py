import random
import art

rand_no=random.randint(1,100)

easy_turns=10
hard_turns=5

def game():
    print(art.logo)
    def guess_number(number,no_of_turns):
        if number > rand_no:
            print("Too High")
            print("Guess Again")
            return no_of_turns -1
        elif number < rand_no:
            print("Too low")
            print("Guess Again")
            return no_of_turns -1
        elif number==rand_no:
            print(f"You got it! The Number was {number}")



    print("Welcome to the number guessing game!")
    print("I'm Thinking of a number between 1 to 100")
    def difficulty():
        level=input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
        if level=="easy":
            return easy_turns
        elif level=="hard":
            return hard_turns

    turns=difficulty()
    user_guess=0
    while user_guess !=rand_no:
        print(f"You have {turns} attempts remaining to guess the number")
        user_guess = int(input("Make a Guess:\n"))
        turns=guess_number(user_guess,turns)

        if turns==0:
            print("Opps You Can't guess Again\nYou've run out of your attempts, You lose!")
            return


game()

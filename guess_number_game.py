# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo_guess

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def compare(answer, guess, turns):
    if guess == answer:
        print(f"You guessed right! The answer was {answer}.")
    elif guess > answer:
        print("Too high")
        turns -= 1
        return turns
    elif guess < answer:
        print("Too low")
        turns -= 1
        return turns


def set_difficulty():
    difficulty = input("Choose difficulty. Easy or Hard: ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo_guess)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"psst.. the answer is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")
        guess = int(input("Make a guess: "))
        turns = compare(answer, guess, turns)
        if turns == 0:
            print(f"You ran out of guesses! I was thinking of {answer}!")
            return
        elif guess != answer:
            print("Guess again")


game()

from art import logo
print(logo)

lets_play = input("Welcome to the Number Guessing Game!!")
thought_of_num = input("I'm thinking of a number between 1 to 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

import random

def thinking_number():
    chosen_number = random.randint(1, 100)
    return chosen_number

secret_number = thinking_number()

def count_down_attempts():
    if difficulty_level == 'easy':
        lives = 10
        print(f"You have {lives} attempts remaining to guess the number.\nMake a guess: ")
        return lives
    elif difficulty_level == 'hard':
        lives = 5
        print(f"You have {lives} attempts remaining to guess the number.")
        return lives
    else:
        print("Pick 'easy' or 'hard'.")
        return difficulty_level

lives = count_down_attempts()

while lives:
    guess = int(input(""))
    if guess == secret_number:
        print("You're correct!")
        break
    else:
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Play again.")
            break
        elif guess > secret_number:
            print(f"Too High. Guess again. \nYou have {lives} attempts remaining to guess the number.\nMake a guess: ")
        elif guess < secret_number:
            print(f"Too low. Guess again. \nYou have {lives} attempts remaining to guess the number.\nMake a guess: ")
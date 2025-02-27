#Max H, Number Guessing Game, you will need to import random for this to work

import random

def do_guess(random_num, user_guess):
    if user_guess > random_num:
        return "Above"
    elif user_guess < random_num:
        return "Lower"
    elif user_guess == random_num:
        return "At"
    elif user_guess < 1:
        print("You can't guess a number below 1.")
        return "None"
    elif user_guess > 1000:
        print("You can't guess a number above 1000")
        return "None"
    
def get_random_num():
    random_num = random.randint(1, 1000)
    return random_num

def check_guess(user_guess, number_of_guesses):
    if user_guess == "Above":
        number_of_guesses + 1
        print("You guessed above the number try again!")
        return number_of_guesses, False
    if user_guess == "Below":
        number_of_guesses + 1
        print("You guessed below the number try again!")
        return number_of_guesses, False
    if user_guess == "At":
        number_of_guesses + 0
        print("You guessed the number! Congratulations!")
        return number_of_guesses, True
    if user_guess == "None":
        number_of_guesses + 0
        return number_of_guesses, False

def number_guessing_game():
    user_has_guessed_number = False
    number_of_guesses = 0
    random_num = get_random_num()
    while user_has_guessed_number == False:
        user_number_guess = input("Please type in your guess (the number is between 1 and 1000): ")
        user_guess = do_guess(random_num, user_number_guess)
        number_of_guesses, user_has_guessed_number = check_guess(user_guess)
    return number_of_guesses
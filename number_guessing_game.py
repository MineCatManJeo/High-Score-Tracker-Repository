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

def check_guess_add_guesses(user_guess, number_of_guesses):
    if user_guess == "Above":
        number_of_guesses = number_of_guesses + 1
        return number_of_guesses
    if user_guess == "Lower":
        number_of_guesses = number_of_guesses + 1
        return number_of_guesses
    if user_guess == "At":
        number_of_guesses + 0
        return number_of_guesses
    if user_guess == "None":
        return number_of_guesses

def check_guess_check_if_guessed(user_guess, number_of_guesses):
    if user_guess == "Above":
        print("You guessed above the number try again!")
        return False
    if user_guess == "Lower":
        print("You guessed below the number try again!")
        return False
    if user_guess == "At":
        print("You guessed the number! Congratulations!")
        return True
    if user_guess == "None":
        return False

def number_guessing_game():
    user_has_guessed_number = False
    number_of_guesses = 0
    random_num = get_random_num()
    while user_has_guessed_number == False:
        user_number_guess = input("Please type in your guess (the number is between 1 and 1000): ")
        if user_number_guess.isnumeric():
            user_number_guess = int(user_number_guess)
            user_guess = do_guess(random_num, user_number_guess)
            number_of_guesses = check_guess_add_guesses(user_guess, number_of_guesses)
            user_has_guessed_number = check_guess_check_if_guessed(user_guess, number_of_guesses)
            print(f"Here are your current and/or final amount of guesses: {number_of_guesses}")
        else:
            print("Please type in a number.")
    return number_of_guesses

number_guessing_game()
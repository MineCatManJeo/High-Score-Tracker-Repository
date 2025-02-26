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

def check_guess(user_guess)

def number_guessing_game():
    random_num = get_random_num()
    user_number_guess = input("Please type in your guess (the number is between 1 and 1000): ")
    user_guess = do_guess(random_num, user_number_guess)
    
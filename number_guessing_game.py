#Max H, Number Guessing Game, you will need to import random for this to work

import random

def do_guess(random_num, user_guess):
    if user_guess > random_num:
        return "Above"
    elif user_guess < random_num:
        return "Lower"
    elif user_guess == random_num:
        return "At"
    
def get_random_num():
    random_num = random.randint(1, 1000)
    return random_num


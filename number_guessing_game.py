#Max H, Number Guessing Game, you will need to import random for this to work

import random

#Getting if the guess is above the number, lower than it, is at the number, and it also includes some error handling
def do_guess(random_num, user_guess, pre_guess):
    close_far, lower_higher = "None", "None"
    if pre_guess != None:
        pre_guess = int(pre_guess)
        if abs(user_guess-random_num) < abs(pre_guess-random_num):
            close_far = 'Closer'
        elif abs(user_guess-random_num) > abs(pre_guess-random_num):
            close_far = 'Further'
    if user_guess > random_num:
        lower_higher = "Above"
    elif user_guess < random_num:
        lower_higher = "Lower"
    elif user_guess == random_num:
        lower_higher = "At"
    elif user_guess < 1:
        print("You can't guess a number below 1.")
        lower_higher = "None"
    elif user_guess > 1000:
        print("You can't guess a number above 1000")
        lower_higher = "None"
    return lower_higher, close_far

#Gets the random number
def get_random_num():
    random_num = random.randint(1, 1000)
    return random_num

#Adding one to the guesses variable if the guess is above or below the number
def check_guess_add_guesses(user_guess, number_of_guesses):
    if user_guess == "Above":
        number_of_guesses += 1
        return number_of_guesses
    if user_guess == "Lower":
        number_of_guesses += 1
        return number_of_guesses
    if user_guess == "At":
        return number_of_guesses
    if user_guess == "None":
        return number_of_guesses

#Checking to see if the user guesses the number
def check_guess_check_if_guessed(user_guess, user_guess_closer):
    if user_guess_closer == "Closer":
        print('Your guess was closer to the number than your previous guess! And:')
    elif user_guess_closer == "Further":
        print('Your guess was further away from the number than your previous guess! And:')
    if user_guess == "Above":
        print(f"You guessed above the number try again!")
        return False
    if user_guess == "Lower":
        print(f"You guessed below the number try again!")
        return False
    if user_guess == "At":
        print("\033cYou guessed the number! Congratulations!")
        return True
    if user_guess == "None":
        return False

#The core game this uses all the previous functions
def number_guessing_game():
    print('\033c')
    user_has_guessed_number = False
    number_of_guesses = 0
    random_num = get_random_num()
    user_number_guess = None

    while user_has_guessed_number == False:
        previous_guess = user_number_guess
        user_number_guess = input("Please type in your guess (the number is between 1 and 1000): ")

        print('\033c')
        if user_number_guess.isnumeric():
            user_number_guess = int(user_number_guess)
            user_guess_above_below, user_guess_closer = do_guess(random_num, user_number_guess, previous_guess)
            number_of_guesses = check_guess_add_guesses(user_guess_above_below, number_of_guesses)
            user_has_guessed_number = check_guess_check_if_guessed(user_guess_above_below, user_guess_closer)
            print(f"Here are your current and/or final amount of guesses: {number_of_guesses}")
        else:
            print("Please type in a number.")
    return number_of_guesses
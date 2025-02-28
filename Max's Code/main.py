#Max H, User Interface / The Main Function

import keyboard_game

import number_guessing_game

import tic_tac_toe_game

import user_profiles

import hs_lead

#The function that holds all the specific games
def game_library():
    high_score_dict = {"Keyboard game score": "Nothin", "Number guessing game score": "Nothin", "Tic tac toe game score": "Nothin"}
    while True:
        user_input = input("""Which game do you want to play?: 
                        1. spacebar presses in a minute (try to press the spacebar as much as possible in a minute)
                        2. number guessing game (try to guess a randomly generated number between 1 and 1000)
                        3. tic tac toe (play tic tac toe with a computer)
                        4. exit""")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                keyboard_game_high_score = keyboard_game.spacebar_per_seconds_game()
                high_score_dict["Keyboard game score"] = keyboard_game_high_score
            elif user_input == 2:
                number_guessing_game_high_score = number_guessing_game.number_guessing_game()
                high_score_dict["Number guessing game score"] = number_guessing_game_high_score
            elif user_input == 3:
                tic_tac_toe_game_high_score = tic_tac_toe_game.tic_tac_toe_game()
                high_score_dict["Tic tac toe game score"] = tic_tac_toe_game_high_score
            elif user_input == 4:
                print("Hope these games were fun! See you next time.")
                break
        else:
            print("Please type in a number.")
    return high_score_dict

#Grouping all the account functions into a single one
def account_management():
    user_profiles.load_user_profiles()
    user_profiles.leaderboard_fixer()
    user_profiles.user_login()
    user_profiles.save_user_profiles()

#The main user interface
def main():
    while True:
        print("1. Game Library")
        print("2. Account Manager")
        print("3. High Scores")
        print("4. Exit")
        user_input = input("Please choose which option you want to do: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                game_library()
            elif user_input == 2:
                account_management()
            elif user_input == 3:
                hs_lead.hs_leaderboard()
            elif user_input == 4:
                print("Hope you had fun using our program!")
                break
            else:
                print("Invalid option please try again.")
        else:
            print("Please type in a number.")
#Max H, User Interface / The Main Function

#Importing all the neccesary files/functions for this program to work
#import keyboard_game

import number_guessing_game
import tic_tac_toe_game
import keyboard_game
import user_profiles
import hs_lead
from add_scores import *



#The function that holds all the specific games
def game_library(user_key):
    high_score_dict = {"keyboard": 0, "guessing": 0, "tic_tac": 0}
    while True:
        user_input = input("""Which game do you want to play?: 
                        1. spacebar presses in a minute (try to press the spacebar as much as possible in a minute)
                        2. number guessing game (try to guess a randomly generated number between 1 and 1000)
                        3. tic tac toe (play tic tac toe with a computer)
                        4. exit\n""").strip()
        if user_input.isnumeric():
            if user_input == '1':
                game_score = keyboard_game.spacebar_per_seconds_game()
                game = 'keyboard'

            elif user_input == '2':
                game_score = number_guessing_game.number_guessing_game()
                game = 'guessing'
                
            elif user_input == '3':
                game_score = tic_tac_toe_game.tic_tac_toe_game()
                game = 'tic_tac'

            elif user_input == '4':
                print("Hope these games were fun! See you next time.")
                break
            else:
                print("You have not selected one of the options.")
            add_scores(user_key,game_score,game)
        else:
            print("Please type in a number.")
        

#The main user interface
def main():
    user_key = user_profiles.user_login()
    while True:
        if user_key == None:
            return
        print("1. Game Library")
        print("2. Account Manager")
        print("3. High Scores")
        print("4. Exit")
        user_input = input("Please choose which option you want to do: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                game_library(user_key)
                        
            elif user_input == 2:
                user_key = user_profiles.user_login()
            elif user_input == 3:
                hs_lead.hs_leaderboard()
                pass
            elif user_input == 4:
                print("Hope you had fun using our program!")
                break
            else:
                print("Invalid option please try again.")
        else:
            print("Please type in a number.")

main()
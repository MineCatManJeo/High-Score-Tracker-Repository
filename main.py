#Max H, User Interface / The Main Function

#Importing all the neccesary files/functions for this program to work
#import keyboard_game

import number_guessing_game
import tic_tac_toe_game
import user_profiles
import hs_lead
import add_scores


#Adding user scores to a list in a format to be added to the leaderboard
def add_scores_to_list(high_scores, list_of_scores):
    list_of_scores.append(high_scores["keyboard"])
    list_of_scores.append(high_scores["guessing"])
    list_of_scores.append(high_scores["tic_tac"])
    return list_of_scores

#Same as above but for games
def add_games_to_list(high_scores, list_of_games):
    for key in high_scores:
        list_of_games.append(key)
    return list_of_games

#The function that holds all the specific games
def game_library():
    high_score_dict = {"keyboard": 0, "guessing": 0, "tic_tac": 0}
    while True:
        user_input = input("""Which game do you want to play?: 
                        1. spacebar presses in a minute (try to press the spacebar as much as possible in a minute)
                        2. number guessing game (try to guess a randomly generated number between 1 and 1000)
                        3. tic tac toe (play tic tac toe with a computer)
                        4. exit\n""")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                if high_score_dict["keyboard"] == 0:
                    high_score_dict["keyboard"] == 10
                    #keyboard_game_high_score = keyboard_game.spacebar_per_seconds_game()
                    #high_score_dict["keyboard"] = keyboard_game_high_score
                else:
                    user_warning_decision = input("Doing this game again WILL OVERWRITE YOUR PREVIOUS SCORE are you sure you want to continue? Y/N: ")
                    if user_warning_decision.lower() == "y":
                        #keyboard_game_high_score = keyboard_game.spacebar_per_seconds_game()
                        #high_score_dict["keyboard"] = keyboard_game_high_score
                        high_score_dict["keyboard"] = 10
                    else:
                        print("Ok cancelling the game.")
                        continue
            elif user_input == 2:
                if high_score_dict["guessing"] == 0:
                    number_guessing_game_high_score = number_guessing_game.number_guessing_game()
                    high_score_dict["guessing"] = number_guessing_game_high_score
                else:
                    user_warning_decision = input("Doing this game again WILL OVERWRITE YOUR PREVIOUS SCORE are you sure you want to continue? Y/N: ")
                    if user_warning_decision.lower() == "y":
                        number_guessing_game_high_score = number_guessing_game.number_guessing_game()
                        high_score_dict["guessing"] = number_guessing_game_high_score
                    else:
                        print("Ok cancelling the game.")
                        continue
            elif user_input == 3:
                if high_score_dict["tic_tac"] == 0:
                    tic_tac_toe_game_high_score = tic_tac_toe_game.tic_tac_toe_game()
                    high_score_dict["tic_tac"] = tic_tac_toe_game_high_score
                else:
                    user_warning_decision = input("Doing this game again WILL OVERWRITE YOUR PREVIOUS SCORE are you sure you want to continue? Y/N: ")
                    if user_warning_decision.lower() == "y":
                        tic_tac_toe_game_high_score = tic_tac_toe_game.tic_tac_toe_game()
                        high_score_dict["tic_tac"] = tic_tac_toe_game_high_score
                    else:
                        print("Ok cancelling the game.")
                        continue
            elif user_input == 4:
                print("Hope these games were fun! See you next time.")
                break
            else:
                print("You have not selected one of the options.")
        else:
            print("Please type in a number.")
    return high_score_dict

#The main user interface
def main():
    user_key = user_profiles.user_login()
    while True:
        print("1. Game Library")
        print("2. Account Manager")
        print("3. High Scores")
        print("4. Exit")
        user_input = input("Please choose which option you want to do: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                list_of_games = []
                list_of_scores = []
                high_scores = game_library()
                list_of_games = add_games_to_list(high_scores, list_of_games)
                list_of_scores = add_scores_to_list(high_scores, list_of_scores)
                for game in list_of_games:
                    if game == "keyboard":
                        add_scores.add_scores_game(user_key, list_of_scores[0], game)
                    elif game == "guessing":
                        add_scores.add_scores_game(user_key, list_of_scores[1], game)
                    elif game == "tic_tac":
                        add_scores.add_scores_game(user_key, list_of_scores[2], game)
                        
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
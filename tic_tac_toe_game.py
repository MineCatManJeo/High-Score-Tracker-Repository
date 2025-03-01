#Max H, Tic Tac Toe Game, random needs to be imported for this to work
import copy
import random

#The tic tac toe board
tic_tac_toe_board = {"first": "Empty", "second": "Empty", "third": "Empty", "fourth": "Empty", "fifth": "Empty", "sixth": "Empty", "seventh": "Empty", "eighth": "Empty", "ninth": "Empty"}

#A function to print the board
def print_board(tic_board):
    print(tic_board["first"], tic_board["second"], tic_board["third"])
    print(tic_board["fourth"], tic_board["fifth"], tic_board["sixth"])
    print(tic_board["seventh"], tic_board["eighth"], tic_board["ninth"])

#A function to add a players spot to the board while including error handling
def check_player_valid_spot(tic_board, player_choice, can_continue):
    if can_continue == True:
        player_choice = player_choice.lower()
        if player_choice in tic_board.keys():
            if tic_board[player_choice] == "Empty":
                tic_board[player_choice] = "O"
                print(f"Successfully put an O in spot {player_choice}.")
                return tic_board, True
            else:
                print("There is already an X or an O in that spot please try again.")
                return tic_board, False
        else:
            print("Invalid choice please try again.")
            return tic_board, False
    else:
        print("Unexpected error has occured you cannot continue playing this streak.")
        return tic_board

#Basically the same thing as the player one but tweaked because its for the computer
def check_computer_valid_spot(tic_board, computer_choice, computer_space_list):
    if computer_choice in computer_space_list:
        if tic_board[computer_choice] == "Empty":
            tic_board[computer_choice] = "X"
            return tic_board, True
        else:
            return tic_board, False
    else:
        return tic_board, False

#Uses the valid player spot checker to add the spot to the board
def player_board_choice(tic_board):
    player_spot_valid = False
    while player_spot_valid == False:
        print_board()
        player_choice = input("Please choose the spot you want to put an O in: ")
        tic_board, player_spot_valid = check_player_valid_spot(tic_board, player_choice)

#Same as above but tweaked for the computer
def computer_board_choice(tic_board, can_continue):
    if can_continue == True:
        computer_spot_valid = False
        computer_space_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
        while computer_spot_valid == False:
            computer_choice = random.choice(computer_space_list)
            tic_board, computer_spot_valid = check_computer_valid_spot(tic_board, computer_choice, computer_space_list)
            return tic_board
    else:
        return tic_board

#Checking if there is a winner
def check_winner(tic_board):
    tic_winner = "Nobody"
    if tic_board["first"] == "O" and tic_board["second"] == "O" and tic_board["third"] == "O":
        tic_winner = "Player"
    elif tic_board["first"] == "O" and tic_board["fourth"] == "O" and tic_board["seventh"] == "O":
        tic_winner = "Player"
    elif tic_board["first"] == "O" and tic_board["fifth"] == "O" and tic_board["ninth"] == "O":
        tic_winner = "Player"
    elif tic_board["second"] == "O" and tic_board["fifth"] == "O" and tic_board["eighth"] == "O":
        tic_winner = "Player"
    elif tic_board["third"] == "O" and tic_board["sixth"] == "O" and tic_board["ninth"] == "O":
        tic_winner = "Player"
    elif tic_board["third"] == "O" and tic_board["fifth"] == "O" and tic_board["seventh"] == "O":
        tic_winner = "Player"
    elif tic_board["fourth"] == "O" and tic_board["fifth"] == "O" and tic_board["sixth"] == "O":
        tic_winner = "Player"
    elif tic_board["seventh"] == "O" and tic_board["eighth"] == "O" and tic_board["ninth"] == "O":
        tic_winner = "Player"
    elif tic_board["first"] == "X" and tic_board["second"] == "X" and tic_board["third"] == "X":
        tic_winner = "Computer"
    elif tic_board["first"] == "X" and tic_board["fourth"] == "X" and tic_board["seventh"] == "X":
        tic_winner = "Computer"
    elif tic_board["first"] == "X" and tic_board["fifth"] == "X" and tic_board["ninth"] == "X":
        tic_winner = "Computer"
    elif tic_board["second"] == "X" and tic_board["fifth"] == "X" and tic_board["eighth"] == "X":
        tic_winner = "Computer"
    elif tic_board["third"] == "X" and tic_board["sixth"] == "X" and tic_board["ninth"] == "X":
        tic_winner = "Computer"
    elif tic_board["third"] == "X" and tic_board["fifth"] == "X" and tic_board["seventh"] == "X":
        tic_winner = "Computer"
    elif tic_board["fourth"] == "X" and tic_board["fifth"] == "X" and tic_board["sixth"] == "X":
        tic_winner = "Computer"
    elif tic_board["seventh"] == "X" and tic_board["eighth"] == "X" and tic_board["ninth"] == "X":
        tic_winner = "Computer"
    return tic_winner

#If there is a winner add to or stop the players winstreak
def add_stop_winstreak(tic_winner, player_winstreak):
    if tic_winner == "Computer":
        return player_winstreak, False
    elif tic_winner == "Player":
        return player_winstreak + 1, True
    else:
        print("Unexpected error occurred.")

#The core game this uses all the previous functions
def tic_tac_toe_game(tic_board):
    player_winstreak = 0
    tic_board_to_get_back_to = copy.deepcopy(tic_board)
    player_can_continue = True
    while player_can_continue == True:
        player_valid_spot = False
        tic_board = computer_board_choice(tic_board, player_can_continue)
        who_has_won = check_winner(tic_board)
        if who_has_won != "Nobody":
            if who_has_won == "Computer":
                player_winstreak, player_can_continue = add_stop_winstreak(who_has_won, player_winstreak)
                tic_board = tic_board_to_get_back_to
                print(f"Sadly you have lost your ending winstreak was: {player_winstreak}")
            elif who_has_won == "Player":
                player_winstreak, player_can_continue = add_stop_winstreak(who_has_won, player_winstreak)
                tic_board = tic_board_to_get_back_to
                print(f"You have won this game another win was added to your winstreak! Your winstreak is: {player_winstreak}")
        print_board(tic_board)
        while player_valid_spot == False:
            user_board_choice = input("The computer has done their turn which which space on the board do you want to put an O in?: ")
            tic_board, player_valid_spot = check_player_valid_spot(tic_board, user_board_choice, player_can_continue)
            print(tic_board)
        who_has_won = check_winner(tic_board)
        if who_has_won == "Computer":
            player_winstreak, player_can_continue = add_stop_winstreak(who_has_won, player_winstreak)
            tic_board = copy.deepcopy(tic_board_to_get_back_to)
            print(f"Sadly you have lost your ending winstreak was: {player_winstreak}")
        elif who_has_won == "Player":
            player_winstreak, player_can_continue = add_stop_winstreak(who_has_won, player_winstreak)
            tic_board = copy.deepcopy(tic_board_to_get_back_to)
            print("You have won this game another win was added to your winstreak!")
    return player_winstreak
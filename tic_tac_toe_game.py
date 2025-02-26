#Max H, Tic Tac Toe Game, random needs to be imported for this to work

import random

tic_tac_toe_board = {"first": "Empty", "second": "Empty", "third": "Empty", "fourth": "Empty", "fifth": "Empty", "sixth": "Empty", "seventh": "Empty", "eighth": "Empty", "ninth": "Empty"}

def print_board(tic_board):
    print(tic_board["first"], tic_board["second"], tic_board["third"])
    print(tic_board["fourth"], tic_board["fifth"], tic_board["sixth"])
    print(tic_board["seventh"], tic_board["eighth"], tic_board["ninth"])

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

def check_computer_valid_spot(tic_board, computer_choice, computer_space_list):
    computer_choice = computer_choice.lower()
    if computer_choice in computer_space_list:
        if tic_board[computer_choice] == "Empty":
            tic_board[computer_choice] = "X"
            return tic_board, True
        else:
            return tic_board, False
    else:
        return tic_board, False

def player_board_choice(tic_board):
    player_spot_valid = False
    while player_spot_valid == False:
        print_board()
        player_choice = input("Please choose the spot you want to put an O in.")
        tic_board, player_spot_valid = check_player_valid_spot(tic_board, player_choice)
        
def computer_board_choice(tic_board, can_continue):
    if can_continue == True:
        computer_spot_valid = False
        computer_space_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
        while computer_spot_valid == False:
            computer_choice = random.choice(computer_space_list)
            tic_board, computer_spot_valid = check_computer_valid_spot(tic_board, computer_choice, computer_space_list)
    else:
        return tic_board

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

def add_stop_winstreak(tic_winner, player_winstreak, can_continue):
    can_continue == False
    if tic_winner == "Computer":
        return player_winstreak, False
    elif tic_winner == "Player":
        return player_winstreak + 1, True
    else:
        print("Unexpected error occurred.")
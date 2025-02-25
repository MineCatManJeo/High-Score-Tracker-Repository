#Max H, Tic Tac Toe Game

import random

tic_tac_toe_board = {"first": "Empty", "second": "Empty", "third": "Empty", "fourth": "Empty", "fifth": "Empty", "sixth": "Empty", "seventh": "Empty", "eighth": "Empty", "ninth": "Empty"}

def print_board(tic_board):
    print(tic_board["first"], tic_board["second"], tic_board["third"])
    print(tic_board["fourth"], tic_board["fifth"], tic_board["sixth"])
    print(tic_board["seventh"], tic_board["eighth"], tic_board["ninth"])

def check_valid_spot(tic_board, player_choice):
    player_choice = player_choice.lower()
    if player_choice in tic_board.keys():
        if tic_board[player_choice] == "Empty":
            tic_board[player_choice] = "O"
            return tic_board, True
        else:
            print("There is already an X or an O in that spot please try again.")
            return tic_board, False
    else:
        print("Invalid choice please try again.")
        return tic_board, False

def player_board_choice(tic_board):
    player_spot_valid = False
    while player_spot_valid == False:
        print_board()
        player_choice = input("Please choose the spot you want to put an O in.")
        tic_board, player_spot_valid = check_valid_spot(tic_board, player_choice)
        
def computer_board_choice(tic_board):
    computer_spot_valid = False
    computer_space_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
    while computer_spot_valid == False:
        computer_choice = random.choice(computer_space_list)
# Gabes Main Test files
import csv
from add_scores import *
from refresh import refresh
def main():
    games = ['keyboard','guessing','tic_tac']
    user_key = input("Who is user?: ")
    while True:
        option = input('1: Game, 2: Exit: ')
        if option == '1':
            game = input('Choose Game: Keyboard, Number Guessing, Tic-Tac: ').lower()
            score = input('Score: ')
            add_scores(user_key,score,game)
                
        elif option == '2':
            break
        elif option.lower() =='refresh':
            refresh(games)

main()
# Gabes Main Test files
from add_scores import *

def main():
    user_key = input("Who is user?: ")
    while True:
        option = input('1: Game, 2: Exit: ')
        if option == '1':
            game = input('Choose Game: Keyboard, Number Guessing, Tic-Tac: ').lower()
            score = input('Score: ')
            add_scores(user_key,score,game)
                
        elif option == '2':
            break

main()
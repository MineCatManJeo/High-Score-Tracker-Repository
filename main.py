# Gabes Main Test files
import csv
from add_scores import add_scores
from refresh import refresh
def main():
    games = ['keyboard','guessing','tic_tac']
    user_key = input("Who is user?: ")
    while True:
        option = input('1: Game, 2: Exit: ')
        if option == '1':
            game = int(input('Choose Game: 1:Keyboard, 2:Number Guessing, 3: Tic Tac Toe: '))
            score = input('Score: ')
            add_scores(user_key,score,game,games)
                
        elif option == '2':
            break
        elif option.lower() =='refresh':
            refresh(games)

main()
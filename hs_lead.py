####
####
####
####
####
#Ethan Blanco, High Score Leaderboard
####
####
####
####
####
import csv
import os

#Function to read leaderboard from CSV file
def read_leaderboard(filename):

    leaderboard_game = []
    leaderboard_user = []
    if not os.path.exists(f'{filename}'):  # Ensure the file exists
        with open(filename, 'w') as file: # Create correctly formatted file if missing
            writer = csv.writer()
            writer.writerow(['user_key','score'])
        return leaderboard_game

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            leaderboard_game.append(row)

    with open('users.csv','r',newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard_user.append(row)

    return leaderboard_game, leaderboard_user

#Main leaderboard function
def hs_leaderboard():
    
    print("Welcome to the High Score Leaderboard!\n")
    while True:
        print("\n1. Spaces Pressed in a Minute")
        print("2. Number Guessing")
        print("3. Tic Tac Toe")
        print("4. Exit")
        hs_interface = input("What specific leaderboard would you like to see? ").strip()
        if hs_interface == "1":
            game_file = "keyboard.csv"
            print("\nWelcome to the Keyboard Clicking Leaderboard!")
        elif hs_interface == "2":
            game_file = "guessing.csv"
            print("\nWelcome to the Number Guessing Leaderboard!")
        elif hs_interface == "3":
            game_file = "tic_tac.csv"
            print("\nWelcome to the Tic Tac Toe Leaderboard!")
        elif hs_interface == "4":
            print("\033cThanks for looking at leaderboards!\n")
            return
        else:
            print("Invalid selection. Please try again.")
            continue
        leaderb_g, leaderb_u = read_leaderboard("game_csv/"+game_file)
        
        while True:
            hs_option = input("""\nWhat would you like to do?
1. See the entire leaderboard.
2. See the top 5 scores.
3. See the #1 score.
4. See a specific score via username.
5. Exit.\n""")

            if hs_option == '1':
                print("\nFull Leaderboard (Saves top 10 leaderboard scores only):")
                if leaderb_g:
                    for row in leaderb_g:
                        print(f"{row[0]}: {row[1]}") # row 0 is the user, row 1 is the score
                else:
                    print("No scores available.")

            elif hs_option == '2':
                print("\nHere's the top five scores!")
                if leaderb_g:
                    for row in leaderb_g[:5]:
                        print(f"{row[0]}: {row[1]}") # row 0 is the user, row 1 is the score
                else:
                    print("No scores available.")

            elif hs_option == '3':
                if leaderb_g:
                    row = leaderb_g[0]
                    print(f"\nTop Score:\n{row[0]}: {row[1]}") # row 0 is the user, row 1 is the score
                else:
                    print("No score available.")

            elif hs_option == '4':
                user_key_key = input("Enter a player's username to see their score:\n").strip()
                for row in leaderb_u:
                    if row[0] == user_key_key:
                        print(f'{row[0]}: {row[1+int(hs_interface)]}') # Gets scores from user profiles, format: user, pass, key_score, guess_score, tic_score
                        break
                else:
                    print("User not found. Please try again.")

            elif hs_option == '5':
                print("Returning to main menu...\n")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
#Run the leaderboard function
####
####
####
####
####
#Remember to call back this function in MAIN: hs_leaderboard()
####
####
####
####
####

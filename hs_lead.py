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

    leaderboard = {}
    if not os.path.exists(filename):  # Ensure the file exists
        open(filename, 'w').close()  # Create empty file if missing
        return leaderboard

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                user, score = row
                try:
                    leaderboard[user] = int(score)
                except ValueError:
                    print(f"Warning: Invalid score format for user {user} in {filename}")
    return leaderboard

#Function to display leaderboard for a selected game
def display_leaderboard(game_file):
    leaderboard = read_leaderboard(game_file)
    return sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)


#Main leaderboard function
def hs_leaderboard():
    
    print("Welcome to the High Score Leaderboard!\n")
    while True:
        print("\n1. Tic Tac Toe")
        print("2. Number Guessing")
        print("3. Keyboard Clicking")
        print("4. Exit")
        hs_interface = input("What specific leaderboard would you like to see? ").strip()
        if hs_interface == "1":
            game_file = "tic_tac.csv"
            print("\nWelcome to the Tic Tac Toe Leaderboard!")
        elif hs_interface == "2":
            game_file = "guessing.csv"
            print("\nWelcome to the Number Guessing Leaderboard!")
        elif hs_interface == "3":
            game_file = "keyboard.csv"
            print("\nWelcome to the Keyboard Clicking Leaderboard!")
        elif hs_interface == "4":
            print("Thank you for using our system, goodbye!")
            return
        else:
            print("Invalid selection. Please try again.")
            continue
        sorted_leaderboard = display_leaderboard(game_file)
        
        while True:
            try:
                hs_option = int(input("""\nWhat would you like to do?
1. See the entire leaderboard.
2. See the top 10 scores.
3. See the top 5 scores.
4. See the top #1 score.
5. See a specific score via username.
6. Exit.\n"""))

                if hs_option == 1:
                    print("\nFull Leaderboard:")
                    if sorted_leaderboard:
                        for user, score in sorted_leaderboard:
                            print(f"{user}: {score}")
                    else:
                        print("No scores available.")
                elif hs_option == 2:
                    print("\nHere's the top ten scores!")
                    if sorted_leaderboard:
                        for user, score in sorted_leaderboard[:10]:
                            print(f"{user}: {score}")
                    else:
                        print("No scores available.")
                elif hs_option == 3:
                    print("\nHere's the top five scores!")
                    if sorted_leaderboard:
                        for user, score in sorted_leaderboard[:5]:
                            print(f"{user}: {score}")
                    else:
                        print("No scores available.")
                elif hs_option == 4:
                    if sorted_leaderboard:
                        user, score = sorted_leaderboard[0]
                        print(f"\nTop Score:\n{user}: {score}")
                    else:
                        print("No scores available.")
                elif hs_option == 5:
                    keyw_user = input("Enter a player's username to see their score:\n").strip()
                    leaderboard = dict(sorted_leaderboard)
                    if keyw_user in leaderboard:
                        print(f"{keyw_user}'s Score: {leaderboard[keyw_user]}")
                    else:
                        print("User not found. Please try again.")
                elif hs_option == 6:
                    print("Returning to main menu...\n")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
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

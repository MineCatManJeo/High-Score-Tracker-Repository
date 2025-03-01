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
leaderboard = {
    "huh": 1500,
    "who": 1450,
    "what": 1400,
    "when": 1350,
    "where": 1300,
    "why": 1250,
    "how": 1200,
    "maybe": 1150,
    "difficulties": 1100,
    "solutions": 1050,
    "inexistant": 1000
} #Placeholder names

#The Relative paths given by Gabriel, for the scores coming from the different games.
#guessing.csv 
#keyboard.csv
#tic_tac.csv

def hs_leaderboard():

    print("Welcome to the High Score Leaderboard!\n")
    while True:
        try:
            hs_interface = (input("What specific leaderboard would you like to see?"))
            print("1. Tic Tac Toe.")
            print("2. Number Guessing.")
            print("3. Keyboard Clicking.")
            print("4. Exit")
        except ValueError:
            print("")
            continue #Restart back

        if hs_interface == "1": #Tic Tac Toe
            print("Welcome to the Tic Tac Toe Leaderboard!")
            hs_tictactoe = int(input("""What would you like to do?
                1. See the entire leaderboard.
                2. See the top 10 scores.
                3. See the top 5 scores.
                4. See the top #1 score.
                5. See a specific score via username.
                6. Exit.\n"""))
            if hs_tictactoe == 1:
                print("\nFull Leaderboard:")
                for user, score in sorted_leaderboard:
                    print(f"{user}: {score}")
                continue #Continue after displaying leaderboard

            elif hs_tictactoe == 2:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:10]:
                    print(f"{user}: {score}")
                continue  #Continue after displaying top 10

            elif hs_tictactoe == 3:
                print("\nHere's the top five scores!")
                for user, score in sorted_leaderboard[:5]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top 5

            elif hs_tictactoe == 4:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:1]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top player

            elif hs_tictactoe == 5:
                while True:  #Keep prompting until valid username is entered
                    keyw_user = input("Enter a player's username to see all of their registered scores:\n").strip()
                    if not keyw_user:
                        print("Search failed, please be more specific and try again.")
                        continue
                    if keyw_user in leaderboard:
                        print(f"{keyw_user}'s Score: {leaderboard[keyw_user]}")
                        break
                    else:
                        print("User not found. Please try again.")
                continue  #Continue after showing score
            elif hs_tictactoe == 6:
                print("Thank you for using our system!\n")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        elif hs_interface == "2": #Num Guessing
            print("Welcome to the Number Guessing Leaderboard!")
            hs_guessing = int(input("""What would you like to do?
                1. See the entire leaderboard.
                2. See the top 10 scores.
                3. See the top 5 scores.
                4. See the top #1 score.
                5. See a specific score via username.
                6. Exit.\n"""))
            if hs_guessing == 1:
                print("\nFull Leaderboard:")
                for user, score in sorted_leaderboard:
                    print(f"{user}: {score}")
                continue #Continue after displaying leaderboard

            elif hs_guessing == 2:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:10]:
                    print(f"{user}: {score}")
                continue  #Continue after displaying top 10

            elif hs_guessing == 3:
                print("\nHere's the top five scores!")
                for user, score in sorted_leaderboard[:5]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top 5

            elif hs_guessing == 4:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:1]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top player

            elif hs_guessing == 5:
                while True:  #Keep prompting until valid username is entered
                    keyw_user = input("Enter a player's username to see all of their registered scores:\n").strip()
                    if not keyw_user:
                        print("Search failed, please be more specific and try again.")
                        continue
                    if keyw_user in leaderboard:
                        print(f"{keyw_user}'s Score: {leaderboard[keyw_user]}")
                        break
                    else:
                        print("User not found. Please try again.")
                continue  #Continue after showing score

            elif hs_guessing == 6:
                print("Thank you for using our system!\n")
                return

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        elif hs_interface == "3": #Keyboard
            print("Welcome to the Keyboard Clicking Leaderboard!")
            hs_keyboard = int(input("""What would you like to do?
                1. See the entire leaderboard.
                2. See the top 10 scores.
                3. See the top 5 scores.
                4. See the top #1 score.
                5. See a specific score via username.
                6. Exit.\n"""))
            if hs_keyboard == 1:
                print("\nFull Leaderboard:")
                for user, score in sorted_leaderboard:
                    print(f"{user}: {score}")
                continue #Continue after displaying leaderboard

            elif hs_keyboard == 2:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:10]:
                    print(f"{user}: {score}")
                continue  #Continue after displaying top 10

            elif hs_keyboard == 3:
                print("\nHere's the top five scores!")
                for user, score in sorted_leaderboard[:5]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top 5

            elif hs_keyboard == 4:
                print("\nHere's the top ten scores!")
                for user, score in sorted_leaderboard[:1]:
                    print(f"{user}: {score}")
                continue #Continue after displaying top player

            elif hs_keyboard == 5:
                while True:  #Keep prompting until valid username is entered
                    keyw_user = input("Enter a player's username to see all of their registered scores:\n").strip()
                    if not keyw_user:
                        print("Search failed, please be more specific and try again.")
                        continue
                    if keyw_user in leaderboard:
                        print(f"{keyw_user}'s Score: {leaderboard[keyw_user]}")
                        break
                    else:
                        print("User not found. Please try again.")
                        continue  #Continue after showing score

            elif hs_keyboard == 6:
                print("Thank you for using our system!\n")
                return

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue  #Restart loop instead of calling function again
        elif hs_interface == "4":
            print("Thank you for using our system, goodbye!")
            continue #Loop back to main function that will be shared with the group soon.
        elif hs_interface == "":
            print("You entered nothing, please try again.")
            continue
        else:
            print("This doesn't work!")
            continue
            
hs_leaderboard()
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

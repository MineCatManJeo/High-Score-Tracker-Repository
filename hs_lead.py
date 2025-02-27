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
leaderboard = ["huh", "who", "what", "when", "where", "why", "how", "maybe", "difficulties", "solutions", "inexistant"]

def hs_leaderboard():
    print("Welcome to the High Score Leaderboard!\n")
    highscore_query = int(input("""What would you like to do?
                1. See the entire leaderboard.
                2. See the top 10 scores.
                3. See a specific score via username.
                4. Exit.\n"""))
    if highscore_query == 1:
        print("Enter the name of the registered leaderboard here")
        return
    elif highscore_query == 2:
        for user in leaderboard:
            
            print(f"Here's the top ten scores! \n{leaderboard}")
            return
    elif highscore_query == 3:
        keyw_user = input("Enter a player's username to see all of their registered scores.\n")
        if not keyw_user:
            print("Search failed, please be more specific and try again.")
            return
        for user in leaderboard:
            
            pass
    elif highscore_query == 4:
        print("Thank you for using our system!\n")
        return
    else:
        print("This doesn't work, try something else or be more specific.\n")
        return

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
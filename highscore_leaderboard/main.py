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

def hs_leaderboard():
    print("Welcome to the High Score Leaderboard!\n")
    highscore_query = int(input("""What would you like to do?
                1. See the entire leaderboard.
                2. See the top 10 scores.
                3. See a specific score via username.
                4. Exit.\n"""))
    if highscore_query == 1:
        print("Enter the name of the leaderboard here")
        return
    if highscore_query == 2:
        pass
    if highscore_query == 3:
        keyw_user = input("Enter a player's username to see all of their registered scores.")
        if not keyw_user:
            print("Search failed, please be more specific and try again.")
            return
        #Named list of leaderboard
    if highscore_query == 4:
        return print("Thank you for using our system!")
    pass

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
#Alex Anderson High Score Tracker

import csv

# Function: user_profiles
def user_profiles():
#     If previous user data exists then
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            users = list(csv_reader)

    except FileNotFoundError:
        users = []

#         Import user data

#     Else/Otherwise:
#         Create an empty user data dictionary
   
#     user_choice equals a Input saying "Do you want to make a new account or access an existing one?: "

#     If user_choice is equal to "access" Then
#         Call access_account function

#     Else if user_choice is equal to "new" Then
#         Call new_account function

#     Return user_profiles[user_key]

# End the function



# Function access_account
#     While true do:
#         username equals a  Input saying to  "Enter your username: "
        
#         If username exists in user_profiles Then
#             password = Input saying to "Enter your password: "
            
#             If password matches user_profiles[username]["password"] Then
#                 user_key equals username
#                 Return user_key
#             Else/Otherwise:
#                 Display "Incorrect password. Try again.”
#         Else/Otherwise:
#             Display "Username not found. Try again."
#         End the while true
# End the function



# Function new_account
#     While true do:
#         username equals a Input saying to "Enter your desired username: "
        
#         If username already exists in user_profiles Then
#             Display "That username is already taken. Try again."
#         Else/Otherwise:
#             password equals a input saying to "Enter your password: "
            
#             #Making empty leaderboard scores for new user
#             leaderboard_one equals []
#             leaderboard_two equals []
#             leaderboard_three equals []
            
#             # Storing user data in dictionary form
#             user_info = {
#                 "password": password,
#                 "leaderboard_one": leaderboard_one,
#                 "leaderboard_two": leaderboard_two,
#                 "leaderboard_three": leaderboard_three
#             }
            
#             # Adding user data to profiles
#             user_profiles[username] is equal to user_info
#             user_key is equal to username
#             Return user_key
#     End the while true
# End the function


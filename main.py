#Alex Anderson High Score Tracker

import csv
import os

# Function access_account
def access_account(users):
    while True:
        username = input("What is your username?: ").strip()
        
        if username not in users:
            print("That username does not exist.")
            continue

        password = ""
            
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
#         
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

def user_profiles():
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            users = list(csv_reader)

    except FileNotFoundError:
        users = []
   
    user_choice = input("Do you want to make a new acount(1) or access a account(2)?: ").strip()

    if user_choice == "2":
        user_key = access_account()
#     If user_choice is equal to "access" Then
#         Call access_account function

#     Else if user_choice is equal to "new" Then
#         Call new_account function

#     Return user_profiles[user_key]

# End the function



username = input("What is your name you want to go by?: ")
password = input("What do you want your password to be?: ")
with open("users.csv", "a", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([username,password,[],[],[]])
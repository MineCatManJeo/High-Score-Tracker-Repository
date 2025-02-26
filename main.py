import csv

# Function to load user profiles from CSV
def load_user_profiles():
    users = {}
    try:
        with open("users.csv", "r", newline="") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 5:
                    username, password = row[0], row[1]
                    leaderboards = [row[2].strip("[]").split(", "), row[3].strip("[]").split(", "), row[4].strip("[]").split(", ")]
                    users[username] = {"password": password, "leaderboard_one": [item.strip() for item in leaderboards[0]], "leaderboard_two": [item.strip() for item in leaderboards[1]], "leaderboard_three": [item.strip() for item in leaderboards[2]]}
    except FileNotFoundError:
        pass
    return users

# Function to save user profiles to CSV
def save_user_profiles(users):
    with open("users.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        for username, data in users.items():
            csv_writer.writerow([username, data["password"], str(data["leaderboard_one"]), str(data["leaderboard_two"]), str(data["leaderboard_three"])] )

# Function to access an account
def access_account(users):
    while True:
        username = input("What is your username?: ").strip()
        if username not in users:
            print("That username does not exist.")
            continue
        
        password = input("Enter your password: ").strip()
        if password == users[username]["password"]:
            print("Login successful!")
            return username
        else:
            print("Incorrect password. Try again.")

# Function to create a new account
def new_account(users):
    while True:
        username = input("Enter your desired username: ").strip()
        if username in users:
            print("That username is already taken. Try again.")
            continue
        
        password = input("Enter your password: ").strip()
        users[username] = {"password": password, "leaderboard_one": [], "leaderboard_two": [], "leaderboard_three": []}
        print("Account created successfully!")
        return username

# Main function to handle user login or account creation
def main():
    users = load_user_profiles()
    
    while True:
        choice = input("Do you want to make a new account (1) or access an account (2)?: ").strip()
        if choice == "1":
            user_key = new_account(users)
            break
        elif choice == "2":
            user_key = access_account(users)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    save_user_profiles(users)
    print(f"Welcome, {user_key}!")

main()

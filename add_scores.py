import csv
def add_scores(user_profiles,user_key,current_score,total_score,current_game):
    pass
with open("test.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[-1])
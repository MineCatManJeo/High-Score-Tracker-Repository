# reloads everything
import csv
def refresh(games):
    for game in range(3):
        with open(f'{games[game]}.csv','w',newline='') as scores:
                writer = csv.writer(scores)
                writer.writerow(['user_key','score'])
import csv

def add_scores_game(user_key,score,game):
    try:
        with open(f'{game}.csv','r') as scores: # This needs to check if more than 10 lines, then if so it needs to SOMEHOW remove the lowest score out of 11
            pass
    except:
        with open(f'{game}.csv','w',newline='') as scores:
            writer = csv.writer(scores)
            writer.writerow(['user_key','score'])
    finally:
        
        with open(f'{game}.csv','a+',newline='') as scores:
            writer = csv.writer(scores)
            writer.writerow([user_key, score])
            reader = csv.reader(scores)
            scores.seek(0)
            next(reader)
            rows = []
            for row in reader:
                rows.append(row)
            rows.sort(key=lambda x: int(x[1]),reverse=True)
        if len(rows) > 10:
            rows.pop(-1)
        with open(f'{game}.csv','w',newline='') as scores:
            writer = csv.writer(scores)
            rows.insert(0,['user_key','score'])
            writer.writerows(rows)
            list()
def add_scores_user(user_key,score,game):
    with open('users.csv','r+',newline='') as scores:
        reader = csv.reader(scores)
        rows = []
        for row in reader:
            if row[0] == user_key:
                row[['keyboard','guessing','tic_tac'].index(game)+2] = score
            rows.append(row)
        writer = csv.writer(scores)
        writer.writerows(rows)
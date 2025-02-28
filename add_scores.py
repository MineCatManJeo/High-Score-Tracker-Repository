import csv

def add_scores(user_key,score,game,games):
    try:
        with open(f'{games[game-1]}.csv','r') as scores: # This needs to check if more than 10 lines, then if so it needs to SOMEHOW remove the lowest score out of 11
            pass
    except:
        with open(f'{games[game-1]}.csv','w',newline='') as scores:
            writer = csv.writer(scores)
            writer.writerow(['user_key','score'])
    finally:
        
        with open(f'{games[game-1]}.csv','a+',newline='') as scores:
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
            print('popped a score')
            rows.pop(-1)
            with open(f'{games[game-1]}.csv','w',newline='') as scores:
                writer = csv.writer(scores)
                rows.insert(0,['user_key','score'])
                writer.writerows(rows)
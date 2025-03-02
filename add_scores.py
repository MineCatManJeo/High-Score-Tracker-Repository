# Gabe's add scores functions
import csv

def add_scores_game(user_key,score,game,sorting):
    try:
        with open(f'game_csv/{game}.csv','r') as scores: # This fails if there is no file, this is just so it can add a new file easily if needed
            pass

    except:
        with open(f'game_csv/{game}.csv','w',newline='') as scores: # If the wasn't a file origionally now there is
            writer = csv.writer(scores)
            writer.writerow(['user_key','score'])

    finally:
        with open(f'game_csv/{game}.csv','a+',newline='') as scores:
            writer = csv.writer(scores)
            writer.writerow([user_key, score]) # Writes the new score

            reader = csv.reader(scores)
            scores.seek(0) # Brings the "cursor" back to the begining
            next(reader)
            rows = []

            for row in reader:
                rows.append(row)
            rows.sort(key=lambda x: int(x[1]),reverse=sorting) # Sorts the rows by largest score

        if len(rows) > 10: # Checks my game file if it has more than 10 lines
            rows.pop(-1) # Deletes the lower score (last one because the last line is always the lowest score)

        with open(f'game_csv/{game}.csv','w',newline='') as scores: # This rewrites the entire file with all of the scores in order (read and ordered before this)
            writer = csv.writer(scores)
            rows.insert(0,['user_key','score'])

            writer.writerows(rows)


def add_scores_user(user_key,score,game,sorting): # Adds the scores onto the score part of the users profile, reads the whole thing, adds the score rewrites the whole file with the score
    with open('users.csv','r',newline='') as scores:
        reader = csv.reader(scores)
        rows = []
        for row in reader:
            try:
                if row[0] == user_key: # goes through each row in the users
                    game_index = ['keyboard','guessing','tic_tac'].index(game)
                    try:
                        if sorting == True:
                            if int(score) > int(row[game_index+2]): # If their new score is higher that the old score
                                row[game_index+2] = score # Add in their new value
                        if sorting == False:
                            if int(score) < int(row[game_index+2]): # If their new score is higher that the old score
                                row[game_index+2] = score # Add in their new value
                    except: 
                        row[game_index+2] = score # If they didn't have any scores add in their new score
                rows.append(row)
            except:
                print('Error in sorting, too many lines in users.csv')
    with open('users.csv','w',newline='') as scores:
        writer = csv.writer(scores)
        scores.seek(0)
        writer.writerows(rows)
def add_scores(user_key,score,game,sorting):
    add_scores_game(user_key,score,game,sorting)
    add_scores_user(user_key,score,game,sorting)
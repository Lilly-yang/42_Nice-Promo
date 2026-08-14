import random


players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
           'kevin', 'Liam']


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    new_list_1 = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {new_list_1}")
    new_list_2 = [n for n in players if n[0].isupper()]
    print(f"New list of capitalized names only: {new_list_2}\n")

    score_dict = {n: random.randint(10, 1000) for n in players}
    print(f"Score dict: {score_dict}")
    score = [v for v in score_dict.values()]
    score_avg = sum(score) / len(score_dict)
    print(f"Score average is {round(score_avg, 2)}")
    score_high = {n: s for n, s in score_dict.items() if s > score_avg}
    print(f"High scores: {score_high}")

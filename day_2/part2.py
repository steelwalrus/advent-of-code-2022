with open('day_2/input.txt', 'r') as file:
    f = file.read().strip()
    inputs = [i.split(' ') for i in f.splitlines()]

def play_rps(pair: list):
    #         rock paper scissors
    # rock      3   6   0
    # paper     0   3   6
    # scissors  6   0   3

    outcome_table = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
    ]

    strategy_guide = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors"
    }

    who_wins = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    score_lookup = {
        0: 1,
        1: 2,
        2: 3
    }

    lookup_codes = {
        "Rock": 0,
        "Paper": 1,
        "Scissors": 2
    }

    first = strategy_guide[pair[0]]
    win_or_lose = who_wins[pair[1]]

    win_index = outcome_table[lookup_codes[first]].index(win_or_lose)
    outcome = outcome_table[lookup_codes[first]][win_index]

    result = outcome + score_lookup[win_index]

    return result

score = 0
for play in inputs:
    score += play_rps(play)

print(score)

# 16098
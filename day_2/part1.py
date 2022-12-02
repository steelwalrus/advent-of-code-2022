with open('2022/day_2/input.txt', 'r') as file:
    f = file.read().strip()
    inputs = [i.split(' ') for i in f.splitlines()]
    # print(inputs)


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
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }

    score_lookup = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    lookup_codes = {
        "Rock": 0,
        "Paper": 1,
        "Scissors": 2
    }

    first = strategy_guide[pair[0]]
    second = strategy_guide[pair[1]]

    outcome = outcome_table[lookup_codes[first]][lookup_codes[second]]
    result = outcome + score_lookup[second]
    # print(f"{first}({score_lookup[first]}) ({pair[0]})[{lookup_codes[first]}] + {second} ({pair[1]})[{lookup_codes[second]}]   (({outcome})) = {result}")
    return result

permutations = []

score = 0
for play in inputs:
    if play not in permutations:
        permutations.append(play)
        print(f"{play}  {play_rps(play)}")
    score += play_rps(play)

print(score)

# 15572

# total score = sum of scores for each round


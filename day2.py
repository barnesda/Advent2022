with open("input/day2.txt") as f:
    games = f.read().splitlines()

# Move + Outcome
point_map_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

point_map_2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}


total_points_1 = 0
total_points_2 = 0
for g in games:
    game_string = g.strip()
    total_points_1 += point_map_1[game_string]
    total_points_2 += point_map_2[game_string]

print(f"Total Points pt1: {total_points_1}")
print(f"Total Points pt2: {total_points_2}")

import re
import math

input_file = open("Day2_Input.txt", 'r', encoding='utf8')


def part_one():
    possible_games = []
    for game, line in enumerate(input_file):
        line_trimmed = line[8:]
        line_split = line_trimmed.split(';')
        sets = len(line_split)
        reds = []
        greens = []
        blues = []
        for set in line_split:
            red_set = [int(s) for s in re.findall(r'(\d+)\s+red', set)]
            reds.extend(red_set)
            green_set = [int(s) for s in re.findall(r'(\d+)\s+green', set)]
            greens.extend(green_set)
            blue_set = [int(s) for s in re.findall(r'(\d+)\s+blue', set)]
            blues.extend(blue_set)

        game_updated = game + 1
        if len(reds) > 0 and len(greens) > 0 and len(blues) > 0:
            if max(reds) <= 12 and max(greens) <= 13 and max(blues) <= 14:
                possible_games.append(game_updated)
        elif len(reds) > 0 and len(greens) > 0:
            if max(reds) <= 12 and max(greens) <= 13:
                possible_games.append(game_updated)
        elif len(reds) > 0 and len(blues) > 0:
            if max(reds) <= 12 and max(blues) <= 14:
                possible_games.append(game_updated)
        elif len(greens) > 0 and len(blues) >0:
            if max(greens) <= 13 and max(blues) <= 14:
                possible_games.append(game_updated)
        elif len(reds) > 0:
            if max(reds) <= 12:
                possible_games.append(game_updated)
        elif len(greens) > 0:
            if max(greens) <= 13:
                possible_games.append(game_updated)
        elif len(blues) > 0:
            if max(blues) <= 14:
                possible_games.append(game_updated)


    print("Possible game sum: ", sum(possible_games))

def part_two():
    powers = []
    for game, line in enumerate(input_file):
        powers_game = []
        line_trimmed = line[8:]
        line_split = line_trimmed.split(';')
        reds = []
        greens = []
        blues = []
        for set in line_split:
            red_set = [int(s) for s in re.findall(r'(\d+)\s+red', set)]
            reds.extend(red_set)
            green_set = [int(s) for s in re.findall(r'(\d+)\s+green', set)]
            greens.extend(green_set)
            blue_set = [int(s) for s in re.findall(r'(\d+)\s+blue', set)]
            blues.extend(blue_set)

        if len(reds) > 0:
            powers_game.append(max(reds))
        if len(greens) > 0:
            powers_game.append(max(greens))
        if len(blues) > 0:
            powers_game.append(max(blues))

        powers.append(math.prod(powers_game))


    print("The sum of all powers is: ", sum(powers))





if __name__ == "__main__":
    #part_one()
    part_two()
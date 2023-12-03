from collections import Counter

def star_one():
    file = open("Day2.txt", "r")
    res = 0
    max_game = Counter()
    max_game["red"] = 12
    max_game["green"] = 13
    max_game["blue"] = 14
    
    for idx, line in enumerate(file):
        game_id = idx + 1
        game_num, handfuls = line.strip().split(":")
        handfuls_list = [h[1:] for h in handfuls.split(";")]
            
        game_count = Counter()
        
        for handful in handfuls_list:
            hand = handful.split(", ")
            for pair in hand:
                num, colour = pair.split(" ")
                num = int(num)
                if colour not in game_count:
                    game_count[colour] = num
                else:
                    game_count[colour] = max(game_count[colour], num)
        if game_count <= max_game:
            res += game_id

    print(res)


def star_two():
    file = open("Day2.txt", "r")
    res = 0

    for line in file:
        game_num, handfuls = line.strip().split(":")
        handfuls_list = [h[1:] for h in handfuls.split(";")]
        game_count = Counter()
        for handful in handfuls_list:
            hand = handful.split(", ")
            for pair in hand:
                num, colour = pair.split(" ")
                num = int(num)
                if colour not in game_count:
                    game_count[colour] = num
                else:
                    game_count[colour] = max(game_count[colour], num)
        power = game_count["red"] * game_count["blue"] * game_count["green"]
        res += power

    print(res)

star_one()
star_two()
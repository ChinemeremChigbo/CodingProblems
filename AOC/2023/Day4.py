def star_one():
    file = open("Day4.txt", "r")
    res = 0
    input = []

    for line in file:
        input.append(line.strip())

    for idx, line in enumerate(input):
        points = 0
        newline = line.split(":")
        winning, other = newline[1].split("|")
        winning = {int(num) for num in winning.split()}
        other = [int(num) for num in other.split()]
        for new_num in other:
            if new_num in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        res += points


    print(res)


def star_two():
    file = open("Day4.txt", "r")
    res = 0
    input = []
    counter = {}
    for idx, line in enumerate(file):
        input.append(line.strip())
        counter[idx+1] = 1
    

    for idx, line in enumerate(input):
        points = 0
        newline = line.split(":")
        winning, other = newline[1].split("|")
        winning = {int(num) for num in winning.split()}
        other = [int(num) for num in other.split()]
        for new_num in other:
            if new_num in winning:
                points += 1
        copies = counter[idx+1]
        for next_num in range(idx+2, idx+2+points):
            if next_num in counter:
                counter[next_num] += 1*copies
    for num in counter:
        res += counter[num]

    print(res)


star_one()
star_two()

def star_one():
    file = open("Day5.txt", "r")
    res = 0
    input = []

    for line in file:
        input.append(line.strip())
    category = []
    seeds = [int(i) for i in input[0].split(":")[1].split()]
    for idx, line in enumerate(input[2:]):
        if line == "" or idx == len(input[2:]) - 1:
            if idx == len(input[2:]) - 1:
                category.append(line)
            for seed_idx, seed in enumerate(seeds):
                for mappings in category[1:]:
                    dest_start, source_start, range_length = [
                        int(i) for i in mappings.split()]
                    if source_start <= seed < source_start + range_length:
                        offset = seed - source_start
                        seeds[seed_idx] = dest_start + offset
            category = []
        else:
            category.append(line)
    res = min(seeds)
    print(res)


def star_two():
    file = open("Day5.txt", "r")
    res = 0
    input = []
    for line in file:
        input.append(line.strip())
    seeds = input[0].split(":")[1].split()
    seed_pairs = [(int(seeds[i]), int(seeds[i])+int(seeds[i+1])-1)
                  for i in range(0, len(seeds), 2)]
    print(seed_pairs)
    category = []
    for idx, line in enumerate(input):
        if line == "" or idx == len(input[2:]) - 1:
            if idx == len(input[2:]) - 1:
                category.append(line)
            for seed_idx, seed_start, seed_end in enumerate(seeds):
                for mappings in category[1:]:
                    dest_start, source_start, range_length = [
                        int(i) for i in mappings.split()]
                    source_end = source_start + range_length - 1
                    if source_end < seed_start or source_start > seed_end:
                        pass
                    elif source_start <= seed_start and source_end >= seed_end:
                        pass
                    elif source_start > seed_start and source_end >= seed_end:
                        pass
                    elif source_start > seed_start and source_end < seed_end:
                        pass
                    # if seed_end >= source_start

                    # if source_start <= seed <= source_end:
                    #     offset = seed - source_start
                    #     seeds[seed_idx] = dest_start + offset
            category = []
        else:
            category.append(line)
    res = min(seeds)
    print(res)


star_one()
star_two()

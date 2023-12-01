file = open("Day1.txt", "r")
res = 0
num_map = {"one":"1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine":"9"}

for line in file:
    first_digit = 0
    last_digit = 0
    for idx, char in enumerate(line):
        # print(char)
        line_length = len(line)
        if char.isnumeric():
            if not first_digit:
                first_digit = char
            last_digit = char
        for num in num_map:
            num_length = len(num)
            if idx + num_length < line_length:
                if line[idx:idx+num_length] == num:
                    if not first_digit:
                        first_digit = num_map[num]
                    last_digit = num_map[num]
    res += (int(first_digit)*10) + int(last_digit)

print(res)

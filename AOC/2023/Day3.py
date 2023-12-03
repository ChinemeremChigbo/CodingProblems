

def star_one():
    file = open("Day3.txt", "r")
    res = 0
    input = []

    for line in file:
        input.append(line.strip())

    input_height = len(input)
    input_width = len(input[0])

    def check(x,y):
        for checkx, checky in ((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)):
            if 0 <= checkx < input_width and 0 <= checky < input_height:
                if not (input[checky][checkx].isnumeric()) and input[checky][checkx] != ".":
                    return True
        return False

    number = 0
    part = False
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char.isnumeric():
                number *= 10
                number += int(char)
                if check(x,y):
                    part = True
            else:
                if number and part:
                    res += number
                number = 0
                part = False
    print(res)



def star_two():
    file = open("Day3.txt", "r")
    res = 0
    input = []

    for line in file:
        input.append(line.strip())

    input_height = len(input)
    input_width = len(input[0])

    def get_number(x, y):
        number_string = ""
        for leftx in range(x, -1, -1):
            if input[y][leftx].isnumeric():
               number_string = input[y][leftx] + number_string
            else: break
        for rightx in range(x+1, input_width):
            if input[y][rightx].isnumeric():
               number_string += input[y][rightx]
            else: break
        return (int(number_string), leftx, y)

    def check(x, y):
        numbers = set()
        for checkx, checky in ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)):
            if 0 <= checkx < input_width and 0 <= checky < input_height:
                if input[checky][checkx].isnumeric():
                    numbers.add(get_number(checkx, checky))
        if len(numbers) != 2:
            return 0
        numbers_list = list(numbers)
        print(numbers_list)
        return numbers_list[0][0] * numbers_list[1][0]
    
    number = 0
    part = False
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "*":
                check_res = check(x, y)
                if check_res:
                    res += check_res
    print(res)

star_one()
star_two()

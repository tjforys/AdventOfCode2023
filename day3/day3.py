def format_file(file):
    lista = open(file, "r").read().split("\n")
    lista_2 = [list(item) for item in lista]
    return lista_2


def check_line_left(line, index):
    number_left = str()
    i = 1
    while (True):
        if index - i > -1:
            char = line[index - i]
            if index - i > - 1:
                if char.isdigit():
                    number_left = char + number_left
                    i += 1
                else:
                    break
            else:
                break
        else:
            break
    return number_left


def check_line_right(line, index):
    number_right = str()
    i = 1
    while (True):
        if index + i < len(line):
            char = line[index + i]
            if index + i < len(line):
                if char.isdigit():
                    number_right = number_right + char
                    i += 1
                else:
                    break
            else:
                break
        else:
            break
    return number_right


def check_line(line, index):
    start = line[index]
    left = check_line_left(line, index)
    right = check_line_right(line, index)
    if start.isdigit():
        return [left+start+right]
    else:
        return left, right


def part_1(file):
    grid = format_file(file)
    sum_list = []
    for line_nr, line in enumerate(grid):
        if line_nr - 1 > -1:
            line_prev = grid[line_nr - 1]
        else:
            line_prev = None
        if line_nr + 1 < len(grid):
            line_next = grid[line_nr + 1]
        else:
            line_next = None
        for char_nr, char in enumerate(line):
            if (not char.isdigit()) and char != ".":
                sum_list.append(check_line_left(line, char_nr))
                sum_list.append(check_line_right(line, char_nr))
                if line_prev:
                    for i in check_line(line_prev, char_nr):
                        if i:
                            sum_list.append(i)
                if line_next:
                    for i in check_line(line_next, char_nr):
                        if i:
                            sum_list.append(i)
    sum_list_format = [int(i) for i in sum_list if i != '']
    return sum(sum_list_format)


def part_2(file):
    grid = format_file(file)
    gear_ratio_list = []
    for line_nr, line in enumerate(grid):
        if line_nr - 1 > -1:
            line_prev = grid[line_nr - 1]
        else:
            line_prev = None
        if line_nr + 1 < len(grid):
            line_next = grid[line_nr + 1]
        else:
            line_next = None
        for char_nr, char in enumerate(line):
            sum_list = []
            if char == "*":
                sum_list.append(check_line_left(line, char_nr))
                sum_list.append(check_line_right(line, char_nr))
                if line_prev:
                    for i in check_line(line_prev, char_nr):
                        if i:
                            sum_list.append(i)
                if line_next:
                    for i in check_line(line_next, char_nr):
                        if i:
                            sum_list.append(i)
            sum_list_format = [int(i) for i in sum_list if i != '']
            if len(sum_list_format) >= 2:
                product = 1
                for i in sum_list_format:
                    product = i * product
                gear_ratio_list.append(product)
    return sum(gear_ratio_list)


print(part_1("day3/puzzle_input.txt"))
print(part_2("day3/puzzle_input.txt"))
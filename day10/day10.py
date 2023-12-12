def format_file(file):
    lista = open(file, "r").read().split("\n")
    return lista


def find_S(file):
    for line_nr, line in enumerate(file):
        if "S" in line:
            return (line_nr, line.find("S"))


def part_1(file):
    file = format_file(file)
    current_coords = find_S(file)
    if file[current_coords[0]-1][current_coords[1]] in ["|", "7", "F"]:
        direction = "up"
    elif file[current_coords[0]+1][current_coords[1]] in ["|", "L", "J"]:
        direction = "down"
    elif file[current_coords[0]][current_coords[1]-1] in ["-", "L", "F"]:
        direction = "left"
    else:
        direction = "right"
    direction_dict = {
        ("left", "L"): "up",
        ("left", "F"): "down",
        ("left", "-"): "left",
        ("right", "7"): "down",
        ("right", "J"): "up",
        ("right", "-"): "right",
        ("up", "7"): "left",
        ("up", "F"): "right",
        ("up", "|"): "up",
        ("down", "|"): "down",
        ("down", "L"): "right",
        ("down", "J"): "left"
        }
    i = 0
    while (True):
        if direction == "down":
            current_coords = (current_coords[0]+1, current_coords[1])
        elif direction == "up":
            current_coords = (current_coords[0]-1, current_coords[1])
        elif direction == "left":
            current_coords = (current_coords[0], current_coords[1]-1)
        else:
            current_coords = (current_coords[0], current_coords[1]+1)
        current_char = file[current_coords[0]][current_coords[1]]
        i += 1
        if current_char == "S":
            return int(i/2)
        direction = direction_dict[(direction, current_char)]


def part_1_2(file):
    file = format_file(file)
    current_coords = find_S(file)
    if file[current_coords[0]-1][current_coords[1]] in ["|", "7", "F"]:
        direction = "up"
    elif file[current_coords[0]+1][current_coords[1]] in ["|", "L", "J"]:
        direction = "down"
    elif file[current_coords[0]][current_coords[1]-1] in ["-", "L", "F"]:
        direction = "left"
    else:
        direction = "right"
    direction_dict = {
        ("left", "L"): "up",
        ("left", "F"): "down",
        ("left", "-"): "left",
        ("right", "7"): "down",
        ("right", "J"): "up",
        ("right", "-"): "right",
        ("up", "7"): "left",
        ("up", "F"): "right",
        ("up", "|"): "up",
        ("down", "|"): "down",
        ("down", "L"): "right",
        ("down", "J"): "left"
        }
    i = 0
    coord_list = []
    while (True):
        coord_list.append(current_coords)
        if direction == "down":
            current_coords = (current_coords[0]+1, current_coords[1])
        elif direction == "up":
            current_coords = (current_coords[0]-1, current_coords[1])
        elif direction == "left":
            current_coords = (current_coords[0], current_coords[1]-1)
        else:
            current_coords = (current_coords[0], current_coords[1]+1)
        current_char = file[current_coords[0]][current_coords[1]]
        i += 1
        if current_char == "S":
            return coord_list
        direction = direction_dict[(direction, current_char)]


def part_2(file):
    coord_list = part_1_2(file)
    file = format_file(file)
    file[find_S(file)[0]] = file[find_S(file)[0]][:find_S(file)[1]] + "7" + file[find_S(file)[0]][find_S(file)[1] + 1:]
    y = 0
    loop_surface = 0
    for line in file:
        wall_through = 0
        x = 0
        for character in line:
            if (y, x) in coord_list and character != "-":
                if character == "|":
                    wall_through += 1
                elif character in ("F", "L"):
                    first_char = character
                else:
                    if first_char == "F" and character == "7":
                        first_char = ''
                    elif first_char == "L" and character == "J":
                        first_char = ''
                    else:
                        wall_through += 1
            if wall_through % 2 == 1 and (y, x) not in coord_list:
                loop_surface += 1
            x += 1
        y += 1
    return loop_surface


file = "day10/puzzle_input.txt"
test_file = "day10/test_puzzle_input.txt"
print(part_1(file))
print(part_2(file))

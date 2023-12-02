def format_file(file):
    lines = [line.removeprefix("Game ") for line in open(file, "r").read().split("\n")]
    lines_divide_id = [line.split(":") for line in lines]
    for line in lines_divide_id:
        line[1] = line[1].split(';')
        for i in range(len(line[1])):
            line[1][i] = line[1][i].split(",")
            for a in range(len(line[1][i])):
                line[1][i][a] = line[1][i][a].removeprefix(" ")
                line[1][i][a] = line[1][i][a].split(" ")
    return lines_divide_id


def part_1(file):
    id_sum = 0
    cube_max_amount = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for id, content in file:
        if_possible = True
        for round in content:
            if if_possible:
                for cube_amount, cube_color in round:
                    if int(cube_amount) > cube_max_amount[cube_color]:
                        if_possible = False
                        break
        if if_possible:
            id_sum += int(id)
    return id_sum


def part_2(file):
    total_sum = 0
    for id, content in file:
        cubes = {
            "red": [],
            "green": [],
            "blue": []
            }
        for round in content:
            for cube_amount, cube_color in round:
                cubes[cube_color].append(int(cube_amount))
        game_power = max(cubes["red"])*max(cubes["green"])*max(cubes["blue"])
        total_sum += game_power
    return total_sum


print(f'Part 1: {part_1(format_file("day2/puzzle_input.txt"))}')
print(f'Part 2: {part_2(format_file("day2/puzzle_input.txt"))}')

def format_file(file):
    lista = [line.rstrip() for line in open(file, "r")]
    return lista


def map_expansion_part_1(file):
    file = format_file(file)
    line_insert = []
    for line_nr, line in enumerate(file):
        if all(i == "." for i in line):
            line_insert.append(line_nr)
    column_insert = []
    for i in range(len(file[0])):
        if all(line[i] == "." for line in file):
            column_insert.append(i)
    for i in reversed(line_insert):
        file.insert(i, len(file[0]) * ".")
    for i in reversed(column_insert):
        for line_nr, line in enumerate(file):
            file[line_nr] = list(file[line_nr])
            file[line_nr].insert(i, ".")
            file[line_nr] = "".join(file[line_nr])
    return file


def map_expansion_part_2(file):
    file = format_file(file)
    line_insert = []
    for line_nr, line in enumerate(file):
        if all(i == "." for i in line):
            line_insert.append(line_nr)
    column_insert = []
    for i in range(len(file[0])):
        if all(line[i] == "." for line in file):
            column_insert.append(i)
    for i in reversed(line_insert):
        for i in range(1000000):
            file.insert(i, len(file[0]) * ".")
    for i in reversed(column_insert):
        for line_nr, line in enumerate(file):
            for i in range(1000000):
                file[line_nr] = list(file[line_nr])
                file[line_nr].insert(i, ".")
                file[line_nr] = "".join(file[line_nr])


def part_1(file):
    distance = 0
    map = map_expansion_part_1(file)
    galaxy_coord_list = []
    for line_nr, line in enumerate(map):
        for character_nr, character in enumerate(line):
            if character == "#":
                galaxy_coord_list.append((line_nr, character_nr))
    res = [(a, b) for idx, a in enumerate(galaxy_coord_list) for b in galaxy_coord_list[idx + 1:]]
    for first, second in res:
        distance += abs(second[0] - first[0]) + abs(second[1] - first[1])
    return int(distance)


def part_2(file):
    distance = 0
    map = map_expansion_part_2(file)
    galaxy_coord_list = []
    for line_nr, line in enumerate(map):
        for character_nr, character in enumerate(line):
            if character == "#":
                galaxy_coord_list.append((line_nr, character_nr))
    res = [(a, b) for idx, a in enumerate(galaxy_coord_list) for b in galaxy_coord_list[idx + 1:]]
    for first, second in res:
        distance += abs(second[0] - first[0]) + abs(second[1] - first[1])
    return int(distance)


def part_2_alt(file):
    file = format_file(file)
    multiplier = 1000000
    total_sum = 0
    galaxy_coord_list = []
    for line_nr, line in enumerate(file):
        for character_nr, character in enumerate(line):
            if character == "#":
                galaxy_coord_list.append((line_nr, character_nr))
    all_pairs = [(a, b) for idx, a in enumerate(galaxy_coord_list) for b in galaxy_coord_list[idx + 1:]]
    for first, second in all_pairs:
        y_list = (first[0], second[0])
        for i in range(min(y_list), max(y_list)):
            if all(character == "." for character in file[i]):
                total_sum += multiplier
            else:
                total_sum += 1
        x_list = (first[1], second[1])
        for i in range(min(x_list), max(x_list)):
            if all(line[i] == "." for line in file):
                total_sum += multiplier
            else:
                total_sum += 1
    return total_sum


file = "day11/puzzle_input.txt"
test_file = "day11/test_puzzle_input.txt"
print(part_1(file))
print(part_2_alt(file))

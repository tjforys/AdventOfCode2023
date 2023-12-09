import time
from math import lcm


def format_file(file):
    lista = open(file, "r").read().split("\n\n")
    lista[1] = [item.split(" = ") for item in lista[1].split("\n")]
    for instr_nr, [source, instr] in enumerate(lista[1]):
        lista[1][instr_nr][1] = lista[1][instr_nr][1].removeprefix("(")
        lista[1][instr_nr][1] = lista[1][instr_nr][1].removesuffix(")")
        lista[1][instr_nr][1] = lista[1][instr_nr][1].split(", ")
    return lista


def part_1(file):
    file = format_file(file)
    instructions = file[0]
    map = file[1]
    position = map[0]
    i = 0
    while (True):
        if position[0] == "ZZZ":
            return i
        command = instructions[i % len(instructions)]
        if command == "L":
            new_dest = position[1][0]
        elif command == "R":
            new_dest = position[1][1]

        for new_pos in map:
            if new_dest == new_pos[0]:
                position = new_pos
                break
        i += 1
        print(position[0])


def part_1_alternate(file):
    start_time = time.time()
    file = format_file(file)
    instructions = file[0]
    map = file[1]
    map_dict = {}
    for line in map:
        map_dict[line[0]] = tuple(line[1])
    position = ("AAA", map_dict["AAA"])
    i = 0
    while (True):
        if position[0] == "ZZZ":
            print("Process finished --- %s seconds ---" % (time.time() - start_time))
            return i
        command = instructions[i % len(instructions)]
        if command == "L":
            new_dest = position[1][0]
        elif command == "R":
            new_dest = position[1][1]
        position = (new_dest, map_dict[new_dest])
        i += 1


def part_2(file):
    file = format_file(file)
    instructions = file[0]
    map = file[1]
    map_dict = {}
    for line in map:
        map_dict[line[0]] = tuple(line[1])
    position_list = [(item[0], item[1]) for item in map if item[0][-1] == "A"]
    i = 0
    while (True):
        command = instructions[i % len(instructions)]
        print(position_list, command)
        if all(item[0][-1] == "Z" for item in position_list):
            return i
        # command = instructions[i % len(instructions)]
        # print(position_list, command)
        for pos_nr, position in enumerate(position_list):
            if command == "L":
                new_dest = position[1][0]
            elif command == "R":
                new_dest = position[1][1]
            position_list[pos_nr] = (new_dest, map_dict[new_dest])
        i += 1


def part_2_testing(file):
    file = format_file(file)
    instructions = file[0]
    map = file[1]
    map_dict = {}
    for line in map:
        map_dict[line[0]] = tuple(line[1])
    position = ("AAA", map_dict["AAA"])
    position_list = [(item[0], item[1]) for item in map if item[0][-1] == "A"]
    i = 0
    cycle_list = []
    for position in position_list:
        sub_cycle_list = []
        while (True):
            if position[0][-1] == "Z":
                sub_cycle_list.append(i)
                if len(sub_cycle_list) > 2:
                    cycle_list.append((position[0], sub_cycle_list[-1]-sub_cycle_list[-2]))
                    break

            command = instructions[i % len(instructions)]
            if command == "L":
                new_dest = position[1][0]
            elif command == "R":
                new_dest = position[1][1]
            position = (new_dest, map_dict[new_dest])
            i += 1
    cycle_list_2 = [item[1] for item in cycle_list]
    return lcm(*cycle_list_2)


file = "day8/puzzle_input.txt"
test_file = "day8/test_puzzle_input.txt"
print(part_2_testing(file))

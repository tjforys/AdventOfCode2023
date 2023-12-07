def format_file_part_1(file):
    lista = open(file, "r").read().split("\n")
    lista_2 = [category.split(" ") for category in lista]
    for category_nr, category in enumerate(lista_2):
        lista_2[category_nr] = [item for item in category if item != '']
    for i in lista_2:
        i.pop(0)
    return lista_2


def format_file_part_2(file):
    lista = open(file, "r").read().split("\n")
    lista_2 = [category.replace(" ", "").split(":") for category in lista]
    for i in lista_2:
        i.pop(0)
    return lista_2


def part_1(file):
    file = format_file_part_1(file)
    ways_record = 1
    time, distance = file
    for race_nr, race in enumerate(time):
        record_list = []
        for race_variant in range(int(race)):
            race_distance = race_variant * (int(race)-race_variant)
            if race_distance > int(distance[race_nr]):
                record_list.append(race_distance)
        ways_record *= len(record_list)
    return ways_record


def part_2(file):
    file = format_file_part_2(file)
    record_list = []
    time, distance = file
    for i in range(int(time[0])):
        race_distance = i * (int(time[0])-i)
        if race_distance > int(distance[0]):
            record_list.append(race_distance)
    return len(record_list)


file = "day6/puzzle_input.txt"
print(part_1(file))
print(part_2(file))

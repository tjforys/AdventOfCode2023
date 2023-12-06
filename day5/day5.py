def format_file(file):
    file = open(file, 'r').read().split('\n\n')
    lista = [item.split('\n') for item in file]
    for category in lista:
        for line_nr, line in enumerate(category):
            if line_nr == 0:
                continue
            else:
                category[line_nr] = category[line_nr].split(" ")
        category.pop(0)
    return lista


def item_convert(source_item, convert_map):
    source_item = int(source_item)
    map_int = [[int(a), int(b), int(c)] for a, b, c in convert_map]
    for destination, source, map_range in map_int:
        if source_item in range(source, source + map_range):
            dest_number = destination + (source_item - source)
            return dest_number
    return source_item


def item_reverse_convert(dest_item, convert_map):
    dest_item = int(dest_item)
    map_int = [[int(a), int(b), int(c)] for a, b, c in convert_map]
    for destination, source, map_range in map_int:
        if dest_item in range(destination, destination + map_range):
            source_number = source + (dest_item - destination)
            return source_number
    return dest_item


def part_1(file):
    file = format_file(file)
    seeds = file[0][0]
    location_list = []
    file.pop(0)
    for seed in seeds:
        for cat_nr, category in enumerate(file):
            if cat_nr == 0:
                soil = item_convert(seed, category)
            if cat_nr == 1:
                fertilizer = item_convert(soil, category)
            if cat_nr == 2:
                water = item_convert(fertilizer, category)
            if cat_nr == 3:
                light = item_convert(water, category)
            if cat_nr == 4:
                temp = item_convert(light, category)
            if cat_nr == 5:
                humidity = item_convert(temp, category)
            if cat_nr == 6:
                location = item_convert(humidity, category)
        location_list.append(location)
    return min(location_list)


def part_2(file):
    file = format_file(file)
    seeds = file[0][0]
    seeds_range_list = []
    for i in range(0, len(seeds), 2):
        seeds_range_list.append((int(seeds[i]), int(seeds[i+1])))
    location_list = []
    file.pop(0)
    for seed_initial, seed_range in seeds_range_list:
        for seed_nr, seed in enumerate(range(seed_initial, seed_initial + seed_range)):
            print(seed_nr)
            location = seed
            for category in file:
                location = item_convert(location, category)
            location_list.append(location)
        return min(location_list)


def part_2_aternate(file):
    file = format_file(file)
    seeds = file[0][0]
    seeds_range_list = []
    file.pop(0)
    for i in range(0, len(seeds), 2):
        seeds_range_list.append((range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]))))
    while (True):
        seed = i
        print(i)
        for category in reversed(file):
            seed = item_reverse_convert(seed, category)
        if any(seed in seedlist for seedlist in seeds_range_list):
            return i
        i += 1


test_lista = [['50', '98', '2'], ['52', '50', '48']]
file = "day5/puzzle_input.txt"
test_file = "day5/test_puzzle_input.txt"
alt_file = "day5/alt_input.txt"
print(part_2_aternate(alt_file))

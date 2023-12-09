def format_file(file):
    file = open(file, "r").read()
    lista = [[int(number) for number in item.split(" ")] for item in file.split("\n")]
    return lista


def part_1(file):
    file = format_file(file)
    sum_total = 0
    for sequence in file:
        sequence_list = [sequence]
        while (True):
            if all(item == 0 for item in sequence_list[-1]):
                break
            next_sub_list = []
            new_sequence = sequence_list[-1]
            for i in range(len(new_sequence) - 1):
                next_sub_list.append(new_sequence[i+1]-new_sequence[i])
            sequence_list.append(next_sub_list)
        for sub_sequence_nr in reversed(range(len(sequence_list)-1)):
            next_value = sequence_list[sub_sequence_nr + 1][-1] + sequence_list[sub_sequence_nr][-1]
            sequence_list[sub_sequence_nr].append(next_value)
        final_value = sequence_list[0][-1]
        sum_total += final_value
    return sum_total


def part_2(file):
    file = format_file(file)
    sum_total = 0
    for sequence in file:
        sequence_list = [sequence]
        while (True):
            if all(item == 0 for item in sequence_list[-1]):
                break
            next_sub_list = []
            new_sequence = sequence_list[-1]
            for i in range(len(new_sequence) - 1):
                next_sub_list.append(new_sequence[i+1]-new_sequence[i])
            sequence_list.append(next_sub_list)
        for sub_sequence_nr in reversed(range(len(sequence_list)-1)):
            next_value = sequence_list[sub_sequence_nr][0] - sequence_list[sub_sequence_nr + 1][0]
            sequence_list[sub_sequence_nr].insert(0, next_value)
        final_value = sequence_list[0][0]
        sum_total += final_value
    return sum_total


file = "day9/puzzle_input.txt"
test_file = "day9/test_puzzle_input.txt"
print(part_1(file))
print(part_2(file))

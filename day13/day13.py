def format_file(file):
    with open(file, "r") as file_handle:
        lista = file_handle.read().split("\n\n")
        row_list = [grid.split("\n") for grid in lista]
        row_list = [list(row) for row in row_list]
        column_list = [[[line[i] for line in grid] for i in range(len(grid[0]))] for grid in row_list]
    return row_list, column_list


def vertical_check_part_1(row_list, column_list):
    for line_y in range(1, len(row_list[0])):
        mirror = True
        list_before = [column for column_id, column in enumerate(column_list) if column_id < line_y]
        list_after = [column for column_id, column in enumerate(column_list) if column_id >= line_y]
        for smaller_side_nr in range(min([len(list_before), len(list_after)])):
            if list_before[-1-smaller_side_nr] != list_after[smaller_side_nr]:
                mirror = False
                break
        if mirror:
            return len(list_before)
    return 0


def horizontal_check_part_1(row_list, column_list):
    for line_x in range(1, len(column_list[0])):
        mirror = True
        list_before = [row for row_id, row in enumerate(row_list) if row_id < line_x]
        list_after = [row for row_id, row in enumerate(row_list) if row_id >= line_x]

        for smaller_side_nr in range(min([len(list_before), len(list_after)])):
            if list_before[-1-smaller_side_nr] != list_after[smaller_side_nr]:
                mirror = False
                break
        if mirror:
            return len(list_before)*100
    return 0


def vertical_check_part_2(row_list, column_list):
    for line_y in range(1, len(row_list[0])):
        error_count = 0
        list_before = [column for column_id, column in enumerate(column_list)
                       if column_id < line_y]
        list_after = [column for column_id, column in enumerate(column_list)
                      if column_id >= line_y]
        for smaller_side_nr in range(min([len(list_before), len(list_after)])):
            # if list_before[-1-smaller_side_nr] != list_after[smaller_side_nr]:
            #     mirror = False
            #     break
            error_count += sum(i != j for i, j in zip(list_before[-1-smaller_side_nr], list_after[smaller_side_nr]))
        if error_count == 1:
            return len(list_before)
    return 0


def horizontal_check_part_2(row_list, column_list):
    for line_x in range(1, len(column_list[0])):
        list_before = [row for row_id, row in enumerate(row_list) if row_id < line_x]
        list_after = [row for row_id, row in enumerate(row_list) if row_id >= line_x]
        error_count = 0
        for smaller_side_nr in range(min([len(list_before), len(list_after)])):
            # if list_before[-1-smaller_side_nr] != list_after[smaller_side_nr]:
            #     mirror = False
            #     break
            error_count += sum(i != j for i, j in zip(list_before[-1-smaller_side_nr], list_after[smaller_side_nr]))
        if error_count == 1:
            return len(list_before)*100
    return 0


def part_1(file):
    row_list_list, column_list_list = format_file(file)
    total_sum = 0
    for grid_nr, row_list in enumerate(row_list_list):
        column_list = column_list_list[grid_nr]
        total_sum += vertical_check_part_1(row_list, column_list)
        total_sum += horizontal_check_part_1(row_list, column_list)
    return total_sum


def part_2(file):
    row_list_list, column_list_list = format_file(file)
    total_sum = 0
    for grid_nr, row_list in enumerate(row_list_list):
        column_list = column_list_list[grid_nr]
        total_sum += vertical_check_part_2(row_list, column_list)
        total_sum += horizontal_check_part_2(row_list, column_list)
    return total_sum


file = "day13/puzzle_input.txt"
test_file = "day13/test_puzzle_input.txt"
print(part_1(file))
print(part_2(file))

file = open("day1/puzzle_input.txt", "r").read().split("\n")
total_sum = 0
digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for line in file:
    number_occs = {}
    if any(x in line for x in digits.keys()):
        first_string_number = len(line)
        last_string_number = -1
        first_string_occ = len(line)
        last_string_occ = -1
    else:
        first_string_number = None
        last_string_number = None
        first_string_occ = None
        last_string_occ = None
    character_start = None
    character_end = None
    character_end_int = None
    character_start_int = None
    if any(x in line for x in digits.keys()):
        for i in digits.keys():
            if line.find(i) < first_string_occ and line.find(i) > -1:
                first_string_occ = line.find(i)
                first_string_number = digits[i]
            if line.rfind(i) > last_string_occ and line.rfind(i) > -1:
                last_string_occ = line.rfind(i)
                last_string_number = digits[i]
    for character_start in line:
        try:
            character_start_int = int(character_start)
            break
        except Exception:
            pass

    for character_end in reversed(line):
        try:
            character_end_int = int(character_end)
            break
        except Exception:
            pass

    if any(x in line for x in digits.keys()):
        try:
            number_occs[first_string_occ] = str(first_string_number)
        except Exception:
            pass
    if any(x in line for x in digits.keys()):
        try:
            number_occs[last_string_occ] = str(last_string_number)
        except Exception:
            pass

    try:
        number_occs[line.find(str(character_start_int))] = str(character_start_int)
    except Exception:
        pass

    try:
        number_occs[line.rfind(str(character_end_int))] = str(character_end_int)
    except Exception:
        pass

    first_char = number_occs[min(number_occs.keys())]
    last_char = number_occs[max(number_occs.keys())]
    number = first_char + last_char
    total_sum += int(number)

print(total_sum)

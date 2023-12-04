def format_file(file):
    main = open(file, "r").read().split("\n")
    lista = [item.removeprefix("Card").lstrip().removeprefix(f'{item_nr+1}: ') for item_nr, item in enumerate(main)]
    lista_2 = [item.split(" | ") for item in lista]
    for card in lista_2:
        card[0] = [number for number in card[0].split(' ') if number != '']
        card[1] = [number for number in card[1].split(' ') if number != '']
    return lista_2


def part_1(file):
    file = format_file(file)
    total_sum = 0
    for winning, mine in file:
        sum_win = sum(number in winning for number in mine)
        if sum_win:
            total_sum += 2**(sum_win-1)
    return total_sum


def part_2(file):
    original_cards = format_file(file)
    current_cards = format_file(file)
    i = 0
    while (True):
        try:
            current_card = current_cards[i]
        except IndexError:
            return len(current_cards)
        current_card_number = original_cards.index(current_card)
        winning, mine = current_card
        sum_win = sum(number in winning for number in mine)
        for add_card in range(sum_win):
            current_cards.append(original_cards[current_card_number+add_card+1])
        i += 1


file = "day4/puzzle_input.txt"
test_file = "day4/test_puzzle_input.txt"
print(part_1(file))
print(part_2(file))

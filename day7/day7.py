def format_file(file):
    lista = open(file, "r").read().split("\n")
    lista_2 = [hand.split(" ") for hand in lista]
    return lista_2


def part_1(file):
    total_sum = 0
    file = format_file(file)
    poker_hands = {
        (5,): 6,
        (1, 4): 5,
        (2, 3): 4,
        (1, 1, 3): 3,
        (1, 2, 2): 2,
        (1, 1, 1, 2): 1,
        (1, 1, 1, 1, 1): 0
        }
    poker_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    for hand_nr, [hand, bet] in enumerate(file):
        poker_hand = tuple(sorted([hand.count(char) for char in set(hand)]))
        hand_value = poker_hands[poker_hand]
        file[hand_nr].append(hand_value)
    file.sort(key=lambda x: (x[2], poker_values[x[0][0]],  poker_values[x[0][1]],  poker_values[x[0][2]],  poker_values[x[0][3]],  poker_values[x[0][4]]))
    for hand_nr, [hand, bet, hand_value] in enumerate(file):
        total_sum += (hand_nr + 1) * int(bet)
    return total_sum


def part_2(file):
    file = format_file(file)
    total_sum = 0
    poker_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1
    }
    poker_hands = {
        (5,): 6,
        (1, 4): 5,
        (2, 3): 4,
        (1, 1, 3): 3,
        (1, 2, 2): 2,
        (1, 1, 1, 2): 1,
        (1, 1, 1, 1, 1): 0
        }
    for hand_nr, [hand, bet] in enumerate(file):
        old_hand = tuple(sorted([hand.count(char) for char in set(hand) if char!= "J"]))
        new_hand = list(old_hand)
        if new_hand:
            new_hand[-1] = new_hand[-1] + 5-sum(new_hand)
        else:
            new_hand.append(5)
        new_hand = tuple(new_hand)
        hand_value = poker_hands[new_hand]
        file[hand_nr].append(hand_value)
    file.sort(key=lambda x: (x[2], poker_values[x[0][0]],  poker_values[x[0][1]],  poker_values[x[0][2]],  poker_values[x[0][3]],  poker_values[x[0][4]]))
    for hand_nr, [hand, bet, hand_value] in enumerate(file):
        total_sum += (hand_nr + 1) * int(bet)
    return total_sum


file = "day7/puzzle_input.txt"
test_file = "day7/test_puzzle_input.txt"
print(part_1(file))
print(part_2(file))
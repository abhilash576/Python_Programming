def is_single_riffle(half1, half2, shuffled_deck):
    half1_index = 0
    half2_index = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    for card in shuffled_deck:

        if half1_index <= half1_max_index and card == half1[half1_index]:
            half1_index += 1
        elif half2_index <= half2_max_index and card == half2[half2_index]:
            half2_index += 1
        else:
            return False

    return True

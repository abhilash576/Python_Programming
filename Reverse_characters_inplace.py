
def reverse(list_of_chars):
    # Reverse the input list of chars in place
    size = len(list_of_chars)
    n = size / 2
    l_index = 0
    r_index = size - 1
    for i in range(n):
        a = list_of_chars[l_index]
        list_of_chars[l_index] = list_of_chars[r_index]
        list_of_chars[r_index] = a
        l_index += 1
        r_index -= 1

    pass

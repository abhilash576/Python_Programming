def get_products_of_all_ints_except_at_index(int_list):
    # Make a list with the products
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    before = [None] * len(int_list)
    prod = 1
    for i in xrange(0, len(int_list)):
        before[i] = prod
        prod = prod * int_list[i]

    prod = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        before[i] = before[i] * prod
        prod = prod * int_list[i]

    return before

def _move_all_zeros_to_the_end(array):

    zero_count = array.count(0)
    original_length = len(array)

    for x in range(zero_count):

        array.remove(0)

    for i in range(original_length - len(array)):

        array.append(0)
    return array


print(_move_all_zeros_to_the_end([5, 0, 4, 0, 2, 7, 0, 0, 2, 9, 8, 5, 2]))

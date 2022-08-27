def _second_largest_number(array):
    array.sort(reverse=True)

    max_1 = array[0]

    for i in array:
        if i != max_1:
            return i


print(_second_largest_number([1, 2, 3, 4, 5, 6, 7, 8]))

def _merge_two_arrays(array_1, array_2):
    list.extend(array_1, array_2)

    return array_1


print(_merge_two_arrays([1, 2, 3, 4, 5, 6, 7], [8, 9]))

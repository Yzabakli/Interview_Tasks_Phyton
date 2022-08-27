def _remove_duplicates(array):
    array.reverse()

    for i in array:

        if array.count(i) > 1:

            for x in range(array.count(i) - 1):
                array.remove(i)

    array.reverse()
    return array


print(_remove_duplicates([1, 1, 2, 2, 3, 3, 4]))

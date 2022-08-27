def _reverse(array):

    _list = []

    i = len(array) - 1

    while i >= 0:

        _list.append(array[i])
        i -= 1

    return _list


print(_reverse([1, 2, 3, 4, 5]))

def _sort_in_ascending_order(array):

    for i in range(len(array)):
        for j in range(i + 1, len(array)):

            if array[j] < array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


print(_sort_in_ascending_order([5, 5, 5, 5, 5, 4, 3, 2, 1, 5]))

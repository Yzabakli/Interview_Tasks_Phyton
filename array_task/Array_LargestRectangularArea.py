def _largest_rectangular_area(array):

    _list = []

    for i in range(len(array)):

        count = 1

        for j in range(i + 1, len(array)):

            if array[j] < array[i]:
                break

            count += 1

        k = i - 1
        while k >= 0:

            if array[k] < array[i]:
                break

            count += 1
            k -= 1

        _list.append(array[i] * count)

    return max(_list)


print(_largest_rectangular_area([6, 2, 5, 4, 5, 1, 6]))

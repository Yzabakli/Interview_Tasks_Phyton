def _largest_rectangular_area(array):

    _max = 0

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

        _max = max(_max, array[i] * count)

    return _max


print(_largest_rectangular_area([6, 2, 5, 4, 5, 1, 6]))

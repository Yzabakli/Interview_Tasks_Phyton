def _largest_sum_contiguous_sub_array(array):
    max_1 = 0

    for i in range(len(array)):
        max_2 = array[i]

        for x in range(i + 1, len(array)):
            max_2 += array[x]
            max_1 = max(max_1, max_2)

    return max_1


print(_largest_sum_contiguous_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

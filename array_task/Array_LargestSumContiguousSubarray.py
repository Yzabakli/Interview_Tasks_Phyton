def _largest_sum_contiguous_sub_array(array):
    _max = 0
    temp = 0
    temp2 = -876606428364086

    for i in array:
        temp2 = max(temp2, i)

    if temp2 <= 0:
        return temp2

    for x in array:
        temp += x
        temp = max(temp, 0)
        _max = max(_max, temp)

    return _max


print(_largest_sum_contiguous_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

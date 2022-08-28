import random


def _sum_up_to_0(n):

    _list = []

    _sum = 0

    for i in range(n - 1):

        _list.append(random.randint(-(n - 1) * 10, (n - 1) * 10))
        _sum += _list[i]

    _list.append(-_sum)
    return _list


print(_sum_up_to_0(6))

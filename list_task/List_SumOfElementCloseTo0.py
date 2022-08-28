import random


def _sum_of_element_close_to_0(array):
    _sum = array[0] + array[1]

    for i in range(len(array)):

        for x in range(i + 1, len(array)):

            if abs(array[i] + array[x]) < abs(_sum):
                _sum = array[i] + array[x]
    return _sum


_list = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
         random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
print(_list)
print(_sum_of_element_close_to_0(_list))

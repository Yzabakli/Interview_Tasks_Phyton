import random


def _add_up_to_sum(array, number):

    sums_dict = {}

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == number:
                sums_dict.setdefault(array[i], array[j])

    print(array)
    print(number)
    print(sums_dict)


_add_up_to_sum([random.randint(0, 12), random.randint(0, 12), random.randint(0, 12), random.randint(0, 12)], 12)

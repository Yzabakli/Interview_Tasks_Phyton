import numbers


def _swap_two_numbers(number_1, number_2):
    number_1 = number_1 + number_2
    number_2 = number_1 - number_2
    number_1 = number_1 - number_2

    return [number_1, number_2]


def _swap_two_numbers_2(number_1, number_2):
    number_1 = number_1 ^ number_2
    number_2 = number_1 ^ number_2
    number_1 = number_1 ^ number_2

    return [number_1, number_2]


print(_swap_two_numbers(75, 50))
print(_swap_two_numbers_2(75, 50))

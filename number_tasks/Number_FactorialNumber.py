def _factorial_number(number):
    if number == 0:
        return 1

    return number * _factorial_number(number - 1)


def _factorial_number_2(number):

    factor = 1
    i = number

    for number in range(number):

        if number != 0:
            factor *= number

    return factor


print(_factorial_number_2(10))

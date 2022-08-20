def _get_count_of_one(number):
    return bin(number).count("1")


def _get_count_of_one_2(number):
    count = 0

    while number > 0:

        if number % 2 != 0:
            count += 1

        number = int(number / 2)

    return count


print(_get_count_of_one_2(16777215))

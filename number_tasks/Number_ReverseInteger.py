def _reverse_integer(num):
    temp = 0

    while int(num) != 0:
        temp = (temp * 10) + (int(num % 10))
        num /= 10

    return int(temp)


print(_reverse_integer(473573657))

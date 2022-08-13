def factorialNumber(number):
    if number == 0:
        return 1

    return number * factorialNumber(number - 1)


def factorialNumber2(number):

    factor = 1
    i = number

    for number in range(number):

        if number != 0:
            factor *= number

    return factor


print(factorialNumber2(10))

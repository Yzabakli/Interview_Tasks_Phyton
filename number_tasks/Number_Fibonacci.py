def _fibonacci(number):

    j = 0
    z = 1

    for i in range(2, number):

        z += j

        j = z - j

    return z


print(_fibonacci(10))

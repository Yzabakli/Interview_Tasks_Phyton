def _is_prime(number):
    if number < 2:
        return 1 == 2

    prime = number == 2 or number == 3 or number == 5 or number == 7
    prime_2 = number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0

    if prime:
        return 1 == 1

    else:
        return prime_2


print(_is_prime(1000551285057161))

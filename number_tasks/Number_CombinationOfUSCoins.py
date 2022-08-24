def _get_count(cents, coin, first_count):
    second_count = 0
    i = 1
    while i * coin <= cents:

        second_count += _combination_of_US_coins(cents - i * coin, coin)
        #second_count += _combination_of_US_coins_2(cents - i * coin, coin)

        i += 1

    second_count += first_count

    return second_count


def _combination_of_US_coins(cents, coin):
    dime = 10
    quarter = 25
    half_dollar = 50

    if cents >= 5:

        count_5 = int(cents / 5)

        if cents >= dime and coin != dime:
            count_10 = _get_count(cents, dime, count_5)

            if cents >= quarter and coin != quarter:
                count_25 = _get_count(cents, quarter, count_10)

                if cents >= half_dollar and coin != half_dollar:
                    count_50 = _get_count(cents, half_dollar, count_25)

                    return count_50 + 1

                else:
                    return count_25 + 1
            else:
                return count_10 + 1
        else:
            return count_5 + 1

    return 1


def _combination_of_US_coins_2(cents, coin):
    coins = [10, 25, 50]
    counts = [0, 0, 0, 0]

    if cents >= 5:
        counts[0] = int(cents / 5)

        i = 0

        while i < len(coins):
            if cents >= coins[i] and coin != coins[i]:
                counts[i + 1] = _get_count(cents, coins[i], counts[i])

            else:
                return counts[i] + 1
            i += 1

        return counts[len(counts) - 1] + 1

    return 1


print(_combination_of_US_coins(100, 0))

def _maximum_profit(array):

    profit = 0

    for i in range(len(array)):

        for x in range(i + 1, len(array)):

            profit = max(profit, array[x] - array[i])

    return profit


print(_maximum_profit([8, 3, 3, 1, 4, 9, 12, 11]))

def _sum_of_left_equal_to_right(array):

    for i in range(len(array)):

        sum_1 = 0
        sum_2 = 0

        for x in range(len(array)):

            if x < i:
                sum_1 += array[x]
            elif x > i:
                sum_2 += array[x]

        if sum_1 == sum_2:
            print(str(array[i]) + " in index " + str(i))


_sum_of_left_equal_to_right([4, 9, 1, 3, 6, 4])

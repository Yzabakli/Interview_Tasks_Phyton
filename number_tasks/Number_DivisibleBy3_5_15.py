def _divisible_by_3_5_15(n):
    divisible_by_15 = []
    divisible_by_5 = []
    divisible_by_3 = []

    for i in range(3, n + 1):

        if i % 15 == 0:

            divisible_by_15.append(str(i))

        elif i % 5 == 0:

            divisible_by_5.append(str(i))

        elif i % 3 == 0:

            divisible_by_3.append(str(i))

    print("Divisible by 15 = [", " ".join(divisible_by_15), "]")
    print("Divisible by 5 = [", " ".join(divisible_by_5), "]")
    print("Divisible by 3 = [", " ".join(divisible_by_3), "]")


_divisible_by_3_5_15(300000)

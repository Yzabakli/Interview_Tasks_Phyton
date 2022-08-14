def _maximum_possible_value(number):
    if number > 0:

        for i in range(len(str(number))):

            if int(str(number)[i]) < 5:
                return int(str.replace(str(number), str(number)[i], "5" + str(number)[i]))

        return int(str(number) + "5")

    elif number < 0:

        for x in range(len(str(-number))):

            if int(str(-number)[x]) > 5:
                return -int(str.replace(str(-number), str(-number)[x], "5" + str(-number)[x]))

        return int(str(number) + "5")

    else:
        return 50


print(_maximum_possible_value(-123))

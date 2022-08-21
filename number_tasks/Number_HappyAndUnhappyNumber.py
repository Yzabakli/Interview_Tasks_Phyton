def _happy_and_unhappy_number(number):
    result = number
    i = 0

    while result != 1:

        i += 1

        if i > 1 and (result == number or result == 37 or result == 20):

            if result != 37 & result != 20:

                print("it reaches again to ", number, " and it took ", i, " round")

            else:
                print("it reaches to 37 or 20 it means it entered in infinite loop")

            return SystemExit

        temp = 0
        temp2 = 0

        for j in str(result):
            temp += pow(int(j), 2)

            if temp2 != len(str(result)) - 1:

                print(j + "² + ", end="")
            else:
                print(j + "² = ", end=""),
            temp2 += 1

        result = temp

        print(result, "\n")

    print(number, " is happy number and it reaches 1 in ", i, " steps")


def _happy_and_unhappy_number_2(number):
    result = number
    i = 0

    while result != 1:

        i += 1

        if i > 1 and (result == number or result == 37 or result == 20):

            print("Unhappy number")

            return SystemExit

        temp = 0

        for j in str(result):
            temp += pow(int(j), 2)

        result = temp

    print("Happy number")


_happy_and_unhappy_number(783)

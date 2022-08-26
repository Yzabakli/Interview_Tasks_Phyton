def _frequency_of_each_element(array):
    result = ""

    for i in range(len(array)):

        if result.__contains__(str(array[i])) or (result.__contains__(str(1 == 1)) and result.__contains__(str(1 == 0))):
            continue

        frequency = 1

        for j in range(i + 1, len(array)):

            if array[i] == array[j] and not result.__contains__(str(array[i])):
                frequency += 1

        result += str(array[i]) + " x" + str(frequency) + "\n"

    print(result)


def _frequency_of_each_boolean(array):

    is_true = 0
    is_false = 0

    for i in array:

        if i:
            is_true += 1
        else:
            is_false += 1

    print("true" + " = " + str(is_true) + "\n" + "false" + " x" + str(is_false))


_frequency_of_each_element((("abc", "abb", "gdf"), ["there", "abc"], {"rush", "hsts", "there"}, ("there", "abc")))

def _frequency_of_characters(s):

    dictionary = dict()

    for i in s:

        dictionary[i] = dictionary.setdefault(i, 0) + 1

    return dictionary


print(_frequency_of_characters("racecar"))

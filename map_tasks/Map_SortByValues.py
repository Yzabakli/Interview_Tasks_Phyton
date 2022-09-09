def _sort_byV_value(dictionary):

    dictionary2 = dict()

    _list = list(dictionary.values())

    _list.sort()

    for i in _list:

        for j in dictionary:

            if dictionary.get(j) == i:

                dictionary2[j] = i

    return dictionary2


print(_sort_byV_value({"name": 4, "age": 3, "gender": 2, "car": 1}))

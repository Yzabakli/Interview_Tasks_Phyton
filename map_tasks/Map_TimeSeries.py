import string


def _time_series(map1, map2):
    map3 = {}

    for y in map1:
        map3[y] = map1[y]

    for key in map2:

        map3[key] = map2.get(key)

        if key in map1:
            map3[key] = map2.get(key) + map1.get(key)

    return map3


print(_time_series({1: 1.0, 2: 1.5, 3: 2.0}, {2: 1.0, 3: 2.5, 5: 1.0}))

import time


def _find_max_number_in_an_array(array):
    max_number = array[0]

    for i in array:

        if i > max_number:
            max_number = i

    return max_number


def _find_min_number_in_an_array(array):
    min_number = array[0]

    for j in array:

        if j < min_number:
            min_number = j

    return min_number


ints = []
for k in range(100000000):
    ints.append(k+1)

start = time.time()
print(_find_max_number_in_an_array(ints))
print(_find_min_number_in_an_array(ints))
print(time.time() - start)

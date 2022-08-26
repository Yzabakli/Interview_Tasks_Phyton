def _permutation(array):
    for i in range(len(array)):
        result = "" + array[i]
        k = 1
        j = i + 1
        while k < len(array):

            if j == len(array):
                j = 0

            result += array[j]
            k += 1
            j += 1
        print(result)
        result = "" + array[i]
        k = 1
        j = i + 2
        while k < len(array):

            if j == i:
                j += 1
            if j >= len(array):
                j = j - len(array)

            result += array[j]
            k += 1
            j += 1
        print(result)


_permutation(['a', 'b', 'c'])

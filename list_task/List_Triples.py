def no_triples(array):
    for i in range(len(array)):

        try:
            if array[i] == array[i + 1] and array[i] == array[i + 2]:
                return 1 == 0
        except IndexError:
            break

    return 0 == 0


print(no_triples([1, 1, 2, 2, 1]))

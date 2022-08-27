def _first_duplicated_element(array):
    for i in range(len(array)):

        for j in range(i + 1, len(array)):

            if array[i] == array[j]:
                return array[i]

    return "all elements are unique"


print(_first_duplicated_element(["1", "2", "3", "4", "5", "6", "6", "7", "8", "9", "0"]))

def _frequency_of_each_element_with_word(array):
    frequency_map = {}

    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    for i in range(len(array)):

        if frequency_map.__contains__(array[i]):
            continue

        frequency = 1

        for j in range(i + 1, len(array)):

            if array[i] == array[j]:
                frequency += 1

        frequency_map.setdefault(array[i], words[frequency])

    return frequency_map


print(_frequency_of_each_element_with_word([1, 2, 3, 4, 3, 2, 1, 3, 2, 2, 2, 4]))

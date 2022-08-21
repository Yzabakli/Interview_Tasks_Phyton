import time


def _lovely_number(a, b):
    if a == b:

        for s in str(a)[:len(str(a)) - 2]:

            if str(a).count(s) > 2:
                return 0

        return 1

    count = int(b - a + 1)

    if a < 1000:
        if b > 1000:

            count -= 9 - (int(a / 111))

        else:
            return int(count - ((b / 111) - (a / 111)))

    for i in range(max(a, 1000), b):

        for s in str(i)[:len(str(i)) - 2]:

            if str(i).count(s) > 2:
                count -= 1
                break

    return count


def _lovely_number_2(a, b):
    lovely_number_count = 0

    if a < 1000:

        lovely_number_count = 1000 - a

        if b > 1000:
            lovely_number_count -= 9 - int(a / 111)

        else:
            return lovely_number_count - (int(b / 111) - int(a / 111))

        a = 1000

    while a <= b:
        digit_frequencies = {}

        digits_as_char_array = str(a)

        for c in digits_as_char_array:
            if digit_frequencies.__contains__(c):
                digit_frequencies.update({c: digit_frequencies[c] + 1})

            else:
                digit_frequencies[c] = 1

            if digit_frequencies[c] > 2:
                break

        if 3 not in digit_frequencies.values():
            lovely_number_count += 1

        a += 1

    return lovely_number_count


start = time.time()
print(_lovely_number_2(1, 4879))
print(time.time() - start)

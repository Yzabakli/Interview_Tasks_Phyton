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


print(_lovely_number(1099, 4879))

def _count_Of_repeated_chars(s):
    temp = ""
    s = s.strip()

    while len(s) > 0:

        count = 1

        i = 1
        for i in range(1, len(s)):

            if s[0] == s[i]:

                count += 1
            else:
                break

        temp += s[0] + str(count)

        s = s[count:]
    return temp


print(_count_Of_repeated_chars("aabcccddaaaa  "))

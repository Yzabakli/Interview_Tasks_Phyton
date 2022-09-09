import math


def _word_break_problem(dictionary, _input):

    m = 10000
    s = _input
    temp = 0

    while 0 == 0:

        i = 0

        while i < len(dictionary):

            m = min(m, len(dictionary[i]))

            if len(s) == 0:

                break

            for j in range(2):

                if s.__contains__(dictionary[i]) and s.index(dictionary[i]) == 0:

                    temp += len(dictionary[i])
                    s = s[len(dictionary[i]):]
            i += 1
        i = len(dictionary) - 1

        while i >= 0:

            if len(s) == 0:
                break

            for j in range(2):

                if s.__contains__(dictionary[i]) and s.index(dictionary[i]) == 0:
                    temp += len(dictionary[i])
                    s = s[len(dictionary[i]):]
            i -= 1
        if temp == len(_input):
            return 0 == 0
        if len(s) < m:
            return 1 == 0


print(_word_break_problem(["leet", "code"], "leetcode"))

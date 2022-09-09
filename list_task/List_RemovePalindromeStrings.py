def _remove_palindrome_strings(_list):
    j = 0

    for i in range(len(_list)):

        r_list = list(_list[j])
        r_list.reverse()
        reverse = "".join(r_list)

        if _list[j] == reverse:

            _list.remove(_list[j])
            j -= 1
        j += 1

    return _list


print(_remove_palindrome_strings(["name", "racecar", "car", "pop", "kototokkototok"]))

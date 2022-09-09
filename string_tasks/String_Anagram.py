def _anagram(s1, s2):

    _set1 = set(s1)
    _set2 = set(s2)
    _list1 = list(_set1)
    _list2 = list(_set2)
    _list1.sort()
    _list2.sort()

    return _list1 == _list2


print(_anagram("amag", "gam"))

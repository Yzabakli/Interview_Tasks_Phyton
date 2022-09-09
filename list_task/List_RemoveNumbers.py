def _remove_numbers(_list):

    for i in _list:

        if i > 100:
            _list.remove(i)

    return _list


print(_remove_numbers([4, 5, 234, 54, 64, 656]))

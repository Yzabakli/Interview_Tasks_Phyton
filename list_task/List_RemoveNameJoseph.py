def _remove_name_joseph(_list):

    while _list.__contains__("Joseph"):
        _list.remove("Joseph")

    return _list


print(_remove_name_joseph(["Joseph", "John", "Eric", "Joseph"]))

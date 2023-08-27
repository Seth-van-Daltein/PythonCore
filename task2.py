mixed_list = ['10', '8', 6, 9, '7', 3, 1, 4, '15', '30']


def func_reverse(item):
    if isinstance(item, str):
        return int(item)
    else:
        return str(item)


converted_list = list(map(func_reverse, mixed_list))

print(converted_list)

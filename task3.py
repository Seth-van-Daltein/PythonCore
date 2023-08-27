lst_from_input = list(map(int, input("Введіть числа через пробіл: ").split()))


def func_lst_to_tuple(lst_to_tuple):
    if len(lst_to_tuple) > 10:
        lst_to_tuple = lst_to_tuple[:10]
    tuple_from_list = tuple(lst_to_tuple)
    return tuple_from_list


result_tuple = func_lst_to_tuple(lst_from_input)
print(result_tuple)

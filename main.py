#                       Завдання № 1

# lst_number_1 = input('Введіть 9 чисел через пробіл: ').split()
#
#
# def dict_generate(lst_1=lst_number_1, lst_2=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     dct = {key: value for key, value in zip(lst_1, lst_2)}
#     print(dct.items())
#     return dct
#
#
# dict_generate(lst_number_1)


#                       Завдання № 2

list_for_keys = input('Введіть 9 значень через пробіл: ').split()
list_for_values = input('Введіть 9 значень через пробіл: ').split()


def return_dict(keys, values):
    if isinstance(keys, list):
        keys = [key for key in keys if not isinstance(key, set)]

    result_dict = {}

    for key in keys:
        result_dict[key] = values

    print(result_dict)
    return result_dict


return_dict(list_for_keys, list_for_values)

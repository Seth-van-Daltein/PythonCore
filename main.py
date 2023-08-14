dct = {
    'person': {'in_dict': [1, 2, 3],
               'after_list': {4, '5'},
               'after_set': ('hello',)
               }
}

new_dict = {}

for key, value in dct.items():
    new_dict[key] = value

    if isinstance(value, dict):
        for inner_key, inner_value in value.items():
            new_dict[inner_key] = inner_value

            if isinstance(inner_value, list):
                for item in inner_value:
                    new_dict[item] = inner_value

            elif isinstance(inner_value, set):
                inner_value_tuple = tuple(inner_value)
                new_dict[inner_value_tuple] = inner_value


print(new_dict)
print(new_dict.keys())

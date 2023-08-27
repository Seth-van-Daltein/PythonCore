mixed_list = ['10', '8', 6, 9, '7', 3, 1, 4, '15', '30']

converted_list = list(map(lambda x: int(x) if isinstance(x, str) and x.isdigit() else str(x), mixed_list))

print(converted_list)

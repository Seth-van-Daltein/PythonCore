# -*- coding: utf-8 -*-

def read_dict_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=')
                    yield (key.strip(), value.strip())
    except Exception as e:
        print(f'Помилка при зчитуванні з файлу: {e}')


# Приклад використання функції-генератора:
filename = 'output.txt'
for pair in read_dict_from_file(filename):
    print(pair)

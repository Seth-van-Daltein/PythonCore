def write_dict_to_file(data_dict, filename):
    try:
        with open(filename, 'w') as file:
            for key, value in data_dict.items():
                file.write(f'{key} = {value}\n')
        print(f'Дані успішно записано у файл {filename}')
    except Exception as e:
        print(f'Помилка при записі у файл: {e}')

# Приклад використання функції:
my_dict = {
    'apple': 'яблуко',
    'banana': 'банан',
    'cherry': 'вишня'
}
write_dict_to_file(my_dict, 'output.txt')

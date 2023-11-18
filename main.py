def count_letters(file_name):
    letter_count = {}

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char_lower = char.lower()
                    if char_lower in letter_count:
                        letter_count[char_lower] += 1
                    else:
                        letter_count[char_lower] = 1
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return letter_count


result = count_letters('your_file.txt')
print(result)

import random


def generate_dict_with_elements():
    # Генеруємо рандомну кількість елементів (в даному прикладі від 1 до 10)
    num_elements = random.randint(1, 10)

    # Створюємо словник, де ключами будуть елементи послідовності, а значеннями - елемент + 1
    result_dict = {element: element + 1 for element in range(1, num_elements + 1)}

    return result_dict


# Приклад виклику функції та виведення результату
generated_dict = generate_dict_with_elements()
print(generated_dict)

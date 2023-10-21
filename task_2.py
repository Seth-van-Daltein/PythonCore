def generate_odd_numbers(limit):
    for number in range(1, limit + 1, 2):  # Генеруємо лише непарні числа
        yield number


# Виводимо перші 3 непарні числа для limit = 10
limit = 10
odd_gen = generate_odd_numbers(limit)

for i in range(3):
    print(next(odd_gen))

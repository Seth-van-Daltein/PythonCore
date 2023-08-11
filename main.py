lst_user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Введіть \'1\' щоб додати елемент в кінець списку')
print('Введіть \'2\' щоб додати елемент в список за індексом')
print('Введіть \'3\' щоб видалити елемент за значенням')
print('Введіть \'4\' щоб визначити індекс елемента за значенням')
print('Введіть \'5\' щоб переглянути весь список')

input_value = int(input('Введіть цифру: '))

if input_value == 1:

    str_or_int = str(input('Введіть, який тип даних який Ви хочете додати(str or int): '))
    if str_or_int == 'str':
        element = str(input('Введіть елемент-стрічку: '))
        lst_user.append(element)
    elif str_or_int == 'int':
        element = int(input('Введіть елемент-число:'))
        lst_user.append(element)
    else:
        print('Error!!!')
    print(lst_user)

elif input_value == 2:

    str_or_int = str(input('Введіть, який тип даних який Ви хочете додати(str or int) за індексом в список: '))
    if str_or_int == 'str':
        element = str(input('Введіть елемент-стрічку: '))
        index = int(input('Введіть індекс куди Ви хочете вставити стрічку: '))
        if element in lst_user:
            y_n = str(
                input('Цей елемент вже існує!!!\nЧи бажаєте ви вставити ще один такий елемент(Введіть yes or no): '))
            if y_n == 'yes':
                lst_user.insert(index, element)
            elif y_n == 'no':
                pass
        else:
            lst_user.insert(index, element)
    elif str_or_int == 'int':
        element = int(input('Введіть елемент-число: '))
        index = int(input('Введіть індекс куди Ви хочете вставити стрічку: '))
        if element in lst_user:
            y_n = str(
                input('Цей елемент вже існує!!!\nЧи бажаєте ви вставити ще один такий елемент(Введіть yes or no): '))
            if y_n == 'yes':
                lst_user.insert(index, element)
            elif y_n == 'no':
                pass
        else:
            lst_user.insert(index, element)
    else:
        print('Error!!!')
    print(lst_user)

elif input_value == 3:

    str_or_int = str(input('Введіть, який тип даних(str or int) який Ви хочете видалити зі списку: '))
    if str_or_int == 'str':
        element = str(input('Введіть елемент-стрічку: '))
        if element in lst_user:
            lst_user.remove(element)
        else:
            print('Такого елемента немає в списку!!!')
    elif str_or_int == 'int':
        element = int(input('Введіть елемент-число: '))
        if element in lst_user:
            lst_user.remove(element)
        else:
            print('Такого елемента немає в списку!!!')
    else:
        print('Error!!!')
    print(lst_user)

elif input_value == 4:

    str_or_int = str(input('Введіть, тип даних(str or int) елемента, індекс якого ви хочете дізнатися: '))
    if str_or_int == 'str':
        element = str(input('Введіть елемент-стрічку: '))
        if element in lst_user:
            a = lst_user.index(element)
            print(a)
        else:
            print('Такого елемента не існує!!!')
    elif str_or_int == 'int':
        element = int(input('Введіть елемент-число: '))
        if element in lst_user:
            a = lst_user.index(element)
            print(a)
        else:
            print('Такого елемента не існує!!!')
    else:
        print('Error!!!')
    print(lst_user)

elif input_value == 5:
    print(lst_user)

else:
    print("Error!!!")

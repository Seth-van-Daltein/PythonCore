import random

# генерація випадкового числа в діапазоні від 5 до 15
rand = random.randrange(5, 15, 1)

lst_user = []

# adding to lst_user random values and random length of lst_user
for i in range(rand):
    i = random.randrange(0, 500, 1)
    lst_user.append(i)
    # print(lst_user)

    # Definition of user role
start = int(input('\t\tPress \'1\' to start: '))

while start == 1:

    print('Натисніть \'1\' щоб вивести всі елементи на екран;')
    print('Натисніть \'2\' щоб редагувати список;')

    number_of_menu = int(input('Press the corresponding key: '))

    while (number_of_menu == 1) or (number_of_menu == 2):

        while number_of_menu == 1:
            print(lst_user)
            number_of_menu += 3

        while number_of_menu == 2:
            print('This action can do only person with role \'Admin\'')
            print('Please, Log in with Admin account!')

            start2 = 1
            while start2 == 1:
                print('\t\tLogin form;')
                login = input('Enter Admin login: ')
                password = int(input('Enter Admin password: '))

                while login.upper() == 'ADMIN' and password == 1234:

                    print('Введіть \'1\' щоб додати елемент в кінець списку')
                    print('Введіть \'2\' щоб додати елемент в список за індексом')
                    print('Введіть \'3\' щоб видалити елемент за значенням')
                    print('Введіть \'4\' щоб визначити індекс елемента за значенням')
                    print('Введіть \'5\' щоб видалити весь список')
                    print('Введіть \'6\' щоб виконати extend')
                    print('Введіть \'7\' щоб скопіювати наявний список')
                    print('Введіть \'8\' щоб дізнатися скільки разів введений Вами елемент буде повторюватися')
                    print('Введіть \'9\' щоб видалити елемент за його індексом')
                    print('Введіть \'10\' щоб виконати reverse')
                    print('Введіть \'11\' щоб сортувати список')
                    print('Введіть \'0\' щоб повернутися назад')

                    print(f'Ваш список: {lst_user}')

                    input_value = int(input('Введіть цифру: '))

                    if input_value == 0:
                        break

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

                        str_or_int = str(
                            input('Введіть, який тип даних який Ви хочете додати(str or int) за індексом в список: '))
                        if str_or_int == 'str':
                            element = str(input('Введіть елемент-стрічку: '))
                            index = int(input('Введіть індекс куди Ви хочете вставити стрічку: '))
                            if element in lst_user:
                                y_n = str(
                                    input(
                                        'Цей елемент вже існує!!!\nЧи бажаєте ви вставити ще один такий елемент(Введіть yes or no): '))
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
                                    input(
                                        'Цей елемент вже існує!!!\nЧи бажаєте ви вставити ще один такий елемент(Введіть yes or no): '))
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

                        str_or_int = str(
                            input('Введіть, який тип даних(str or int) який Ви хочете видалити зі списку: '))
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

                        str_or_int = str(
                            input('Введіть, тип даних(str or int) елемента, індекс якого ви хочете дізнатися: '))
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

                        lst_user.clear()
                        print(f'Ваш список: {lst_user}')

                    elif input_value == 6:

                        str_or_int = str(input('Введіть, який тип даних який Ви хочете додати(str or int): '))
                        if str_or_int == 'str':
                            element = input('Введіть декілька елементів-стрічок через пропуск: ').split()
                            lst_user.extend(element)
                        elif str_or_int == 'int':
                            element = map(int, input('Введіть декілька елементів-чисел через пропуск: ').split())
                            lst_user.extend(element)
                        else:
                            print('Error!!!')
                        print(lst_user)

                    elif input_value == 7:

                        name = str(input('Введіть назву нового списку одним словом: '))
                        lst_copy = lst_user.copy()
                        print(f'Скопійований список: {name} {lst_copy}')

                    elif input_value == 8:

                        str_or_int = str(input('Введіть, який тип даних(str or int): '))
                        if str_or_int == 'str':
                            element = str(input('Введіть який елемент-стрічку Ви хочете порахувати: '))
                            print(f'Данний елемент повторюється {lst_user.count(element)} разів')
                        elif str_or_int == 'int':
                            element = int(input('Введіть який елемент-число Ви хочете порахувати: '))
                            print(f'Данний елемент повторюється {lst_user.count(element)} разів')
                        else:
                            print('Error!!!')
                        print(lst_user)

                    elif input_value == 9:

                        index = int(input('Введіть індекс елемента, який ви хочете видалити: '))
                        print(f'Ви видалили елемент зі значенням {lst_user[index]}')
                        lst_user.pop(index)
                        print(f'Оновлений список: {lst_user}')

                    elif input_value == 10:

                        lst_user.reverse()
                        print(f'Перевернутий список: {lst_user}')

                    elif input_value == 11:

                        lst_sort_int = []
                        lst_sort_str = []

                        for i in lst_user:
                            if type(i) == int:
                                lst_sort_int.append(i)
                            elif type(i) == str:
                                lst_sort_str.append(i)

                        lst_sort_int.sort()
                        lst_sort_str.sort()

                        sorted_lst = []
                        sorted_lst.extend(lst_sort_int)
                        sorted_lst.extend(lst_sort_str)
                        print('')
                        print(sorted_lst)
                        print('')

                else:
                    break

                break

            else:
                break

else:
    print('Error!!!')
    exit(0)

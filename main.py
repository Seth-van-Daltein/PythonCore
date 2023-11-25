class DataClass:
    def __init__(self):
        self.data_dict = {}
        self.data_tuple = ()
        self.admin = False

    def login(self, username, password):
        if username == "admin" and password == "password":
            self.admin = True
        else:
            print("Неправильний логін або пароль")

    def logout(self):
        self.admin = False

    def add_to_dict(self, key, value):
        if key in self.data_dict:
            change = input("Ключ вже існує. Чи бажаєте змінити значення? (y/n) ")
            if change.lower() == 'y':
                self.data_dict[key] = value
        else:
            self.data_dict[key] = value

    def add_to_tuple(self, value):
        if self.admin:
            self.data_tuple += (value,)
        else:
            print("Тільки адмін може додавати значення до кортежу")

    def view_dict(self):
        print(self.data_dict)

    def view_tuple(self):
        print(self.data_tuple)

    def menu(self):
        while True:
            print("1. Логін")
            print("2. Вивести словник")
            print("3. Вивести кортеж")
            print("4. Додати до словника")
            print("5. Додати до кортежу")
            print("6. Вийти")
            choice = input("Виберіть опцію: ")
            if choice == '1':
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                self.login(username, password)
            elif choice == '2':
                self.view_dict()
            elif choice == '3':
                self.view_tuple()
            elif choice == '4':
                key = input("Введіть ключ: ")
                value = input("Введіть значення: ")
                self.add_to_dict(key, value)
            elif choice == '5':
                value = input("Введіть значення: ")
                self.add_to_tuple(value)
            elif choice == '6':
                break
            else:
                print("Невірний вибір")

data = DataClass()
data.menu()

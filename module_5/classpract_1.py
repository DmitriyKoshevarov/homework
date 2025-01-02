from random import choice


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self,username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    @staticmethod
    def password_validation(password):
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
                break

        has_upper = False
        for char in password:
            if char.isupper():
                has_upper = True

        if has_digit == True and has_upper == True:
            print("Пароль корректный")
        else:
            print("Пароль должен содержать хотя бы одну букву в верхнем регистре и хотя бы одну цифру.")
            exit()


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую, выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Неверный пароль.")
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "),password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз.")
                continue
            User.password_validation(password)
            database.add_user(user.username, user.password)
        print(database.data)


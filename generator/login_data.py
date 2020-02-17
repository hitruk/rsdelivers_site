from random import choice
import json


class GeneratorLogin:

    DATA_LOGIN = []  # полный набор данных логин для регистрации

    BOUNDARY_VALUE = [4, 5, 6, 63, 64, 65]  # граничные значения (5=<login<=63)
    ERROR_BOUNDARY_VALUE = 'Ошибка: Логин должен содержать минимум 5 знаков'  # если len(login) < 5

    SIZE_LOGIN = 63  # допустимое количество символов в поле логин (5=<SIZE_LOGIN<=63), устанавливать можно любое значение в указанном промежутке
    ERROR_SIZE_LOGIN = 'Ошибка: Логин не должен содержать пробелов, пожалуйста, удалите все пробелы'

    NO_DATA_AVAILABLE_LOGIN = ['', ' ']
    ERROR_STATIC_LOGIN = 'Ошибка: Пожалуйста, введите логин'

    def __init__(self, string):
        self.string = string

    def static_data_login(self):
        data_static_login = [
            (self.string.ascii_lowercase, ''),
            (self.string.ascii_uppercase, ''),
            (self.string.digits, ''),
            ('-635272900', ''),
            (self.string.punctuation, ''),
            (self.string.hexdigits + self.string.punctuation, '')
        ]

        return data_static_login

    def boundary_value_login(self):
        data_generated_login = []
        for row in self.BOUNDARY_VALUE:
            generated_login = ''.join(
                choice(self.string.ascii_letters + self.string.digits + self.string.punctuation) for _ in range(row))
            if len(generated_login) == 4:
                data_generated_login.append((generated_login, self.ERROR_BOUNDARY_VALUE))
            else:
                data_generated_login.append((generated_login, ''))
        return data_generated_login

    def space_in_username(self):
        username_space = []
        for row in range(self.SIZE_LOGIN):
            user = ''.join(choice(self.string.hexdigits) for _ in range(row))
        if len(user) == self.SIZE_LOGIN - 1 and user not in username_space:
            user_one = ' ' + user
            user_two = user + ' '
            user_three = user[0:2] + ' ' + user[2:]
            username_space.append((user_one, self.ERROR_SIZE_LOGIN))
            username_space.append((user_two, self.ERROR_SIZE_LOGIN))
            username_space.append((user_three, self.ERROR_SIZE_LOGIN))
        return username_space

    def no_data_available_login(self):
        no_data_login = []
        for row in self.NO_DATA_AVAILABLE_LOGIN:
            no_data_login.append((row, self.ERROR_STATIC_LOGIN))
        return no_data_login

    def data_login(self):

        self.DATA_LOGIN = self.static_data_login() + self.boundary_value_login() + self.space_in_username() + self.no_data_available_login()

        login_json_path = 'generator/login_error_data.json'
        login_data_json = dict(self.DATA_LOGIN)

        with open(login_json_path, 'w') as file:
            json.dump(login_data_json, file, indent=2, ensure_ascii=False)  # json кириллица  ensure_ascii=False

        return self.DATA_LOGIN
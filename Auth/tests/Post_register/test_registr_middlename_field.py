import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from Auth.methods.payloads import Payloads
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@allure.epic('Post/registration Проверка поля middle name')
class TestRegistrationMiddlenameField:

    @allure.description('Проверка поля middle name - 1 символ')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'A', phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'A', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'A', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 2 символа')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'Aa', phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Кириллица')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'Ффффф', phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ффффф', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ффффф', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Латиница')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'Aaaaaa', phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaaa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaaa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 63 символа')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwww',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name,
                'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwww',
                phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name,
                'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwww',
                phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 64 символа')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwwww',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name,
                'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwwww',
                phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name,
                'Aaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqaaaaaaaaaqwwww',
                phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Пробел')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaa A',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa A', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa A', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Тире')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaa-A',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa-A', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa-A', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Текст в верхнем регистре')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'ВВВВВ',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Текст в нижнем регистре')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'ввввв',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Текст в верхнем и нижнем регистре')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Вввввв',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Вввввв', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Вввввв', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 2 пробела подряд')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Ввввв  В',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв В', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв В', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 2 тире подряд')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Ввввв--В',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв-В', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв-В', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Пустое поле')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, '', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, '', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 65 Символов')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'ФффффффффйФффффффффйФффффффффйФффффффффйФффффффффйФффффффффйууууу',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля middle name - Латиница + Кириллица')
    def test_16(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Ффффaaa',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля middle name - 3 пробела подряд')
    def test_17(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Ввввв   В',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв В', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв В', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - 3 тире подряд')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Ввввв---В',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Ввввв-В', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Ввввв-В', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Цифры')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '0123456',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля middle name - Спецсимволы')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '@#$%^',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля middle name - Начинается пробелом')
    def test_21(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            ' Aaaaa',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Заканчивается пробелом')
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaa ',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Начинается с "тире"')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '-Aaaaa',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Заканчивается "тире"')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaa-',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, 'Aaaaa', phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, 'Aaaaa', phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля middle name - Null')
    def test_25(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            None,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 201)


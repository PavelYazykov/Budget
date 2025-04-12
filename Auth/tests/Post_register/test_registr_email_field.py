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
@allure.epic('Post/registration Проверка поля email')
class TestRegistrationEmailField:

    @allure.description('Проверка поля email - Валидный email')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, email, date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - 64 символа в локальной части')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru',
                last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone,
                'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru',
                date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - спецсимволы в локальной части email')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'z!2$%^&*qa@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'z!2$%^&*qa@mail.ru', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, 'z!2$%^&*qa@mail.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Цифры')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '123456789@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                '123456789@mail.ru', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, '123456789@mail.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Текст в верхнем регистре')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'QWERTYUIOP@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'QWERTYUIOP@mail.ru', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, 'QWERTYUIOP@mail.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Текст в нижнем регистре')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyuiop@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'qwertyuiop@mail.ru', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, 'qwertyuiop@mail.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - 254 символа общая длина email')  # Будет падать: "Mail use not real domain"
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
            'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
            'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560A'
                'aQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
                last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone,
                'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
                'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email- Кириллица')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'йцукенгшщз@почта.рф', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'йцукенгшщз@почта.рф', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, 'йцукенгшщз@почта.рф', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Латиница')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'asdfghjkl@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'asdfghjkl@mail.ru', last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, 'asdfghjkl@mail.ru', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - 159 символов доменная часть')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.testtest12testtest12test'
            'test12testtest12testtest12testtest12123.com',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)  # Будет падать: "Mail use not real domain"
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                'testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.testtest12testtest'
                '12testtest12testtest12testtest12testtest12123.com',
                last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone,
                'testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.testtest12testtest12'
                'testtest12testtest12testtest12testtest12123.com', date_of_birth
            )
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - 65 символов в локальной части')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz101234@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - 255 символа общая длина email')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560Aa'
            'Q1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.A'
            'aQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ123255.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Латиница + Кириллица')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'йцукен@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Пробелы')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer @mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email  - Содержит две точки подряд')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer..@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Содержит две тире подряд')
    def test_16(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer--@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Отсутствие @ в email')
    def test_17(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwermail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Отсутствие локальной части')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Отсутствие доменной части')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Локальная часть начинается  с точки')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '.qwer@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Локальная часть заканчивается точкой')
    def test_21(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui.@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Доменная часть начинается  с точки')
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer@.mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Доменная часть заканчивается точкой')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer@mail..ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Локальная часть начинается  с тире')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '-qwertyui@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Локальная часть заканчивается тире')
    def test_25(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'aaqwertyui-@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Доменная часть начинается  с тире')
    def test_26(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@-mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email- Доменная часть заканчивается тире')
    def test_27(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@mail-.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Пустое поле')
    def test_28(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Существующий email')
    def test_29(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'y.pawel_test1@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 400)

    @allure.description('Проверка поля email - Null')
    def test_29(self):
        """Регистрация"""
        result = AuthMethods.registration(
            None,
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)


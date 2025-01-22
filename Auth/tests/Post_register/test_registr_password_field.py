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
@allure.epic('Проверка поля password')
class TestRegistrationPasswordField:

    @allure.description('12 символов')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, 'Automation@1', last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('100 символов')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'AutomationAutomationAutomationAutomationAutomationAutomation'
            'AutomationAutomationAutomationAutomati@1',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('100 символов')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'Automation @1',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('11 символов')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'Automatio@1',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('101 символ')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'AutomationAutomationAutomationAutomationAutomationAutomation'
            'AutomationAutomationAutomationAutomati@11',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            '',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            None,
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Пароль не соответствует требованиям')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'qwertyusdfghj123',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 400)

    @allure.description('Неверный тип данных (integer)')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            123456789963852,
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Скомпрометированный пароль')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            'qwertyusdfghj123A@',
            last_name,
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 400)

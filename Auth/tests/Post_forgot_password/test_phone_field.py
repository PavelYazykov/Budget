import allure
import pytest

from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
import time
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
not_verify_phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth
verify_phone = AuthVariables.phone
verify_email = AuthVariables.email


@pytest.mark.Auth
@allure.epic('Post_forgot_password Проверка поля phone')
class TestPhoneField:

    @allure.description('Проверка поля phone - Запрос на верифицированный номер телефона')
    def test_01(self):
        """Запрос кода"""
        time.sleep(62)
        result = AuthMethods.forgot_password(verify_phone, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля phone - Поле отсутствует')
    def test_02(self):
        """Запрос кода"""
        time.sleep(62)
        result = AuthMethods.forgot_password_without_phone(verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля phone - Null')
    def test_03(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля phone - Запрос на неверифицированный номер телефона')
    def test_04(self):
        """Создание пользователя"""
        time.sleep(61)
        result_create = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, not_verify_phone, date_of_birth
        )
        Checking.check_statuscode(result_create, 201)
        try:
            """Запрос кода"""
            result = AuthMethods.forgot_password(not_verify_phone, None)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 403)
        except AssertionError:
            raise AssertionError
        finally:
            AuthMethods.delete_user(email)

    @allure.description('Проверка поля phone - Запрос на несуществующий номер телефона')
    def test_05(self):
        """Запрос кода"""

        result = AuthMethods.forgot_password('80000000000', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля phone - Невалидный номер телефона')
    def test_06(self):
        result = AuthMethods.forgot_password('80000000000123', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Пустое поле')
    def test_07(self):
        result = AuthMethods.forgot_password('', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Неверный тип данных integer')
    def test_08(self):
        result = AuthMethods.forgot_password(89260000002, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)





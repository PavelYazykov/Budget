import time
import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
email = AuthVariables.email
password = AuthVariables.password
phone = AuthVariables.phone


@pytest.mark.Auth
@allure.epic('Post/reset_password Проверка поля phone')
class TestResetPasswordCheckPhone:

    @allure.description('Номера запроса кода и при сбросе пароля совпадают')
    def test_01(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(phone, None, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Поле отсутствует')
    def test_02(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password_without_phone(email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Null')
    def test_03(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Номера запроса кода и при сбросе пароля не совпадают')
    def test_04(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password('89260000009', None, password)
        Checking.check_statuscode(result_change, 404)

    @allure.description('Неверный формат номерa')
    def test_05(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password('892600000099', None, password)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пустое поле')
    def test_06(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password('', None, password)
        Checking.check_statuscode(result_change, 422)




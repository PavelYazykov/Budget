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
@allure.epic('Post_reset_password/code_check Проверка поля phone')
class TestCheckPhoneField:

    @allure.description('Проверка поля phone - Номера запроса кода и проверки кода совпадают')
    def test_01(self):

        """Запрос кода на смену пароля"""
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

    @allure.description('Проверка поля phone - Номера запроса кода и проверки кода не совпадают')
    def test_02(self):

        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check('89260000009', None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 404)  # Возможно надо будет поменять статус код

    @allure.description('Проверка поля phone - Неверный формат номера')
    def test_03(self):

        """Запрос кода на смену пароля"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check('892600000099', None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля phone - Поле отсутствует')
    def test_04(self):

        """Запрос кода на смену пароля"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check_without_phone(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля phone - Null')
    def test_05(self):
        """Запрос кода на смену пароля"""
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

    @allure.description('Проверка поля phone - Пустое поле')
    def test_06(self):
        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check("", None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

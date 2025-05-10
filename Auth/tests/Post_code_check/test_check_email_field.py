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
@pytest.mark.check_email_field
@allure.epic('Post_reset_password/code_check Проверка поля email')
class TestCheckEmailField:

    @allure.description('Проверка поля email - email адрес запроса и проверки кода совпадают')
    def test_01(self):
        time.sleep(61)
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля email - Поле отсутствует')
    def test_02(self):
        time.sleep(61)
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check_without_email(result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля email - Null')
    def test_03(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля email - email адрес запроса и проверки кода не совпадают')
    def test_04(self):
        time.sleep(61)
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check('y.pawel_test1@yahoo.ru', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 404)

    @allure.description('Проверка поля email - Неверный формат email')
    def test_05(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check('y.pawel_test1mail.ru', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля email - Пустое поле')
    def test_06(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check('', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)
        time.sleep(61)







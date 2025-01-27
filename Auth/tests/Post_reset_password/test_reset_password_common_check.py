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
@allure.epic('Post_reset_password/reset_password Общие проверки')
class TestResetPasswordCommonCheck:

    @allure.description('Изменение пароля с валидными данными и после кода подтверждения')
    def test_01(self):
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

    @allure.description('Изменение пароля без кода подтверждения')
    def test_02(self):

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(email, password)

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 404)

    @allure.description('Отсутствует body')
    def test_03(self):
        """Изменение пароля"""
        result_change = AuthMethods.reset_password_without_body()

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

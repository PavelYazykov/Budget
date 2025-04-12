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
@allure.epic('Post/reset_password Проверка поля email')
class TestResetPasswordCheckEmail:

    @allure.description('email адрес запроса кода и email при проверке пароля совпадают')
    def test_01(self):
        """Запрос кода"""
        time.sleep(61)
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
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        result_change = None
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password_without_email(password)
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля email - Null')
    def test_03(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        result_change = None
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password(None, password)
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('email адрес запроса кода и email при проверке пароля не совпадают')
    def test_04(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        result_change = None
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password('y.pawel_test1@yahoo.ru', password)
            Checking.check_statuscode(result_change, 404)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля email - Неверный формат email')
    def test_05(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        result_change = None
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password('pawel_test_1rambler.ru', password)
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля email - Пустое поле')
    def test_06(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        result_change = None
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password('', password)
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

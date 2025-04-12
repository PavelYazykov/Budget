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
@allure.epic('Post/reset_password Проверка поля password')
class TestResetPasswordCheckPassword:

    @allure.description('Проверка поля password - 12 символов')
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
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password(email, 'Aa1!tyhgvooa')
            Checking.check_statuscode(result_change, 200)
        finally:
            """Восстановление изначального пароля"""
            result_change = AuthMethods.reset_password(email, password)
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - 100 символов')
    def test_02(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa'
                             '1@111111Aa1@111111Aa1@111111'
            )
            Checking.check_statuscode(result_change, 200)
        finally:
            """Восстановление изначального пароля"""
            result_change = AuthMethods.reset_password(email, password)
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Пробел')
    def test_03(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Zx@1 kjgtreqpbd'
            )
            Checking.check_statuscode(result_change, 200)
        finally:
            """Восстановление изначального пароля"""
            result_change = AuthMethods.reset_password(email, password)
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Ввод предыдущего пароля')
    def test_04(self):
        """Запрос кода"""
        result = AuthMethods.forgot_password(email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)
        try:
            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Zx@1 kjgtreqpbd'
            )
            Checking.check_statuscode(result_change, 200)
        finally:
            """Восстановление изначального пароля"""
            result_change = AuthMethods.reset_password(email, password)
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - 11 символов')
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
            result_change = AuthMethods.reset_password(
                email, 'Zx@1vbytrew'
            )
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - 101 символов')
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
            result_change = AuthMethods.reset_password(
                email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1'
                             '@111111Aa1@111111Aa1@1111112'
            )
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Пустое поле')
    def test_07(self):
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
            result_change = AuthMethods.reset_password(
                email, ''
            )
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Null')
    def test_08(self):
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
            result_change = AuthMethods.reset_password(
               email, None
            )
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Пароль не соответствует требованиям')
    def test_09(self):
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
            result_change = AuthMethods.reset_password(
                email, 'zxcvbnmghqwertyu'
            )
            Checking.check_statuscode(result_change, 400)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Неверный тип данных (integer)')
    def test_10(self):
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
            result_change = AuthMethods.reset_password(
                email, 123456789963852741
            )
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Поле отсутствует')
    def test_11(self):
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
            result_change = AuthMethods.reset_password_without_password(email)
            Checking.check_statuscode(result_change, 422)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля password - Скомпрометированный пароль')
    def test_12(self):
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
            result_change = AuthMethods.reset_password(
                email, 'qwertyuiopA@123'
            )
            Checking.check_statuscode(result_change, 400)
        finally:
            """Восстановление изначального пароля"""
            if result_change.status_code == 200:
                result_change = AuthMethods.reset_password(email, password)
                Checking.check_statuscode(result_change, 200)

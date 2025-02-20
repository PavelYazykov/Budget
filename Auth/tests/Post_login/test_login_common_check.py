import json

import allure
import pytest

from Auth.methods.payloads import Payloads
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
phone = AuthVariables.phone
date_of_birth = AuthVariables.date_of_birth
payloads = AuthVariables.auth_payloads


@pytest.mark.Auth
@allure.epic('Post_reset_password/login Общие проверки')
class TestLoginCommonCheck:

    @allure.description('Создание и авторизация верифицированного пользователя')
    def test_01(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        try:
            """Получение user_id"""
            data = Checking.get_data(create_result)
            user_id = data['id']

            """Верификация пользователя"""
            request_code = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(request_code, 200)
            code = AuthMethods.get_verify_code(request_code)

            verify = AuthMethods.verify(user_id, code)
            Checking.check_statuscode(verify, 200)

            """Авторизация"""
            result_login = AuthMethods.login(
                '11113', f'username={email}&password={password}'
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_login, 200)

            """Проверка наличия обязательных полей"""
            with allure.step('Проверка наличия обязательных полей'):
                Payloads.check_required_fields(result_login, Payloads.required_fields_login)
        except AssertionError:
            raise AssertionError
        finally:
            AuthMethods.delete_user(email)

    @allure.description('Повторный вход без предварительного выхода')
    def test_02(self):
        result = AuthMethods.login(
            '11111', payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Авторизация с нового устройства')
    def test_03(self):
        result = AuthMethods.login(
            '11112', payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Пользователь не верифицирован')
    def test_04(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        try:
            result_login = AuthMethods.login(
                '11113', f'username={email}&password={password}'
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_login, 403)
        except AssertionError:
            raise AssertionError
        finally:
            AuthMethods.delete_user(email)

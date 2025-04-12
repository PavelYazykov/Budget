import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
password = AuthVariables.password


@pytest.mark.Auth
@allure.epic('Post_change_password Проверка поля new_password')
class TestNewPasswordField:

    @allure.description('Проверка поля new_password - 12 символов')
    def test_01(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на смену пароля"""
            result_change = AuthMethods.change_password(
                password, 'Ohranatrud@3', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля new_password - 100 символов')
    def test_02(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на смену пароля"""
            result_change = AuthMethods.change_password(
                password,
                '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
                '1234567Aa@',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля new_password - Пробел')
    def test_03(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на смену пароля"""
            result_change = AuthMethods.change_password(
                password,
                'Ohranatruda@ 2',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля new_password - Проверка на скомпроментированность')
    def test_04(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на смену пароля"""
            result_change = AuthMethods.change_password(
                password,
                '12345679Qwerty@',
                access_token
            )

            """Проверка статус кода"""
            AuthMethods.change_password_back(result_change, '12345679Qwerty@', password, access_token)
            Checking.check_statuscode(result_change, 400)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля new_password - 11 символов')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            'Ohranatru@2',
            access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, 'Ohranatru@2', password, access_token)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля new_password - 101 символ')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
            '1234567Aa@1234567Aa@Z',
            access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(
            result_change,
            '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
            '1234567Aa@1234567Aa@Z',
            password,
            access_token)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля new_password - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            '',
            access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, '', password, access_token)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля new_password -  Поле отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password_without_new_password(password, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля new_password -  Null')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля new_password -  Пароль не соответствует требованиям')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password, 'ohranatruda3', access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, 'ohranatruda3', password, access_token)
        Checking.check_statuscode(result_change, 400)


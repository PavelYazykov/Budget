import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
password = AuthVariables.password


@pytest.mark.Auth
@allure.epic('Post_change_password Проверка поля new_password')
class TestNewPasswordField:

    @allure.description('12 символов')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password, 'Ohranatrud@3', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Восстановление старого пароля"""
        with allure.step('Восстановление старого пароля'):
            result_change = AuthMethods.change_password(
                'Ohranatrud@3', password, access_token
            )
            print('RESULT', result_change.json())
            Checking.check_statuscode(result_change, 200)

    @allure.description('100 символов')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
            '1234567Aa@',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Восстановление старого пароля"""
        with allure.step('Восстановление старого пароля'):
            result_change = AuthMethods.change_password(
                '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
                '1234567Aa@1234567Aa@',
                password,
                access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('Пробел')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            'Ohranatruda@ 2',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Восстановление старого пароля"""
        with allure.step('Восстановление старого пароля'):
            result_change = AuthMethods.change_password(
                'Ohranatruda@ 2',
                password,
                access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка на скомпроментированность')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password,
            '12345679Qwerty@',
            access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, '12345679Qwerty@', password, access_token)
        Checking.check_statuscode(result_change, 400)

    @allure.description('11 символов')
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

    @allure.description('101 символ')
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

    @allure.description('Пустое поле')
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

    @allure.description('Поле отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password_without_new_password(password, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Null')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            password, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пароль не соответствует требованиям')
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


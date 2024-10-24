import allure

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

old_password = 'Ohranatruda@2'


@allure.epic('Post_change_password Проверка поля new_password')
class TestNewPasswordField:

    @allure.description('12 символов')
    def test_01(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password, 'Ohranatruda@3', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Восстановление старого пароля"""
        with allure.step('Восстановление старого пароля'):
            result_change = AuthMethods.change_password(
                'Ohranatruda@3', 'Ohranatruda@2', access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('100 символов')
    def test_02(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
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
                'Ohranatruda@2',
                access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('Пробел')
    def test_03(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
            'Ohranatruda@ 2',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Восстановление старого пароля"""
        with allure.step('Восстановление старого пароля'):
            result_change = AuthMethods.change_password(
                'Ohranatruda@ 2',
                'Ohranatruda@2',
                access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка на скомпроментированность')
    def test_04(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
            '1234567Aa@123456 7Aa',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)

    @allure.description('11 символов')
    def test_05(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
            'Ohranatru@2',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('101 символ')
    def test_06(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
            '1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@1234567Aa@'
            '1234567Aa@1234567Aa@Z',
            access_token
        )

        """Проверка статус кода"""
        status_code = Checking.check_statuscode(result_change, 422)

    @allure.description('Пустое поле')
    def test_07(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password,
            '',
            access_token
        )

        """Проверка статус кода"""
        status_code = Checking.check_statuscode(result_change, 422)

    @allure.description('Поле отсутствует')
    def test_08(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password_without_new_password(old_password, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Null')
    def test_09(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пароль не соответствует требованиям')
    def test_10(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            old_password, 'ohranatruda3', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)


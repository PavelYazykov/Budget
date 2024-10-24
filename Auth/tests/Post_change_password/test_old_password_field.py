import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

old_password = 'Ohranatruda@2'


@allure.epic('Post_change_password Проверка поля old_password')
class TestOldPasswordField:

    @allure.description('Старый пароль - неверный')
    def test_01(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            'Ohranatruda@1111', 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)

    @allure.description('Пустое поле')
    def test_02(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            '', 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Поле отсутсвует')
    def test_03(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password_without_old_password(
            'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Null')
    def test_04(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            None, 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)


import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
password = AuthVariables.password


@pytest.mark.Auth
@allure.epic('Post_change_password Проверка поля old_password')
class TestOldPasswordField:

    @allure.description('Проверка поля old_password - Старый пароль - неверный')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            'Ohranatruda@1111', 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, 'Ohranatruda@1', password, access_token)
        Checking.check_statuscode(result_change, 400)

    @allure.description('Проверка поля old_password - Пустое поле')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            '', 'Ohranatruda@2', access_token
        )

        """Проверка статус кода"""
        AuthMethods.change_password_back(result_change, 'Ohranatruda@2', password, access_token)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля old_password - Поле отсутсвует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password_without_old_password(
            'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)

    @allure.description('Проверка поля old_password - Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на смену пароля"""
        result_change = AuthMethods.change_password(
            None, 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 422)


import allure
import pytest
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods


@pytest.mark.Auth
@allure.epic('Post_reset_password/login Проверка поля username')
class TestCheckUsernameField:

    @allure.description('Проверка поля username - Несуществующий username')
    def test_01(self):
        result = AuthMethods.login(
            '11111', 'username=ya%40mail.ru&password=Ohranatruda@1'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля username - Пустое поле')
    def test_02(self):
        result = AuthMethods.login(
            '11111', 'username=&password=Ohranatruda@1'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля username - Поле отсутствует')
    def test_03(self):
        result = AuthMethods.login(
            '11111', 'password=Ohranatruda@1'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля username - Null')
    def test_05(self):
        result = AuthMethods.login(
            '11111', 'username=null&password=Ohranatruda@1'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

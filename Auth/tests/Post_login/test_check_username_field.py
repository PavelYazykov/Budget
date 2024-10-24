import allure

from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods


@allure.epic('Post_reset_password/login Проверка поля username')
class TestCheckUsernameField:

    @allure.description('Несуществующий username')
    def test_01(self):
        result = AuthMethods.login(
            '11111', 'username=ya%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Пустое поле')
    def test_02(self):
        result = AuthMethods.login(
            '11111', 'username=&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_03(self):
        result = AuthMethods.login(
            '11111', 'password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_05(self):
        result = AuthMethods.login(
            '11111', 'username=null&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

import allure

from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods


@allure.epic('Post_reset_password/login Проверка поля password')
class TestCheckPasswordField:

    @allure.description('Неверный пароль')
    def test_01(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1@mail.ru&password=Ohranatruda@111'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Пустое поле')
    def test_02(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1@mail.ru&password='
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_03(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1@mail.ru'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_04(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1@mail.ru&password=null'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

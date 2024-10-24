import allure

from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
import time

verify_phone = '89260000002'
not_verify_phone = '89260000004'
verify_email = 'pawel_test_1@rambler.ru'
not_verify_email = 'bmk20284@nowni.com'


@allure.epic('Post_forgot_password Проверка поля email')
class TestEmailField:

    @allure.description('Запрос на верифицированную почту')
    def test_01(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Поле отсутствует')
    def test_02(self):
        time.sleep(62)
        result = AuthMethods.forgot_password_without_email(verify_phone)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Null')
    def test_03(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(verify_phone, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Запрос на неверифицированную почту')
    def test_04(self):
        result = AuthMethods.forgot_password(None, not_verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

    @allure.description('Запрос на несуществующую почту')
    def test_05(self):
        result = AuthMethods.forgot_password(None, 'qwertyzxcvbasdfg123@gmail.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Невалидная почта')
    def test_06(self):
        result = AuthMethods.forgot_password(None, 'qwertyu.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_07(self):
        result = AuthMethods.forgot_password(None, '')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

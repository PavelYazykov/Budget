import allure

from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
import time

verify_phone = '89260000002'
not_verify_phone = '89260000004'
verify_email = 'pawel_test_1@rambler.ru'


@allure.epic('Post_forgot_password Проверка поля phone')
class TestPhoneField:

    @allure.description('Запрос на верифицированный номер телефона')
    def test_01(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(verify_phone, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Поле отсутствует')
    def test_02(self):
        time.sleep(62)
        result = AuthMethods.forgot_password_without_phone(verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Null')
    def test_03(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(None, verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Запрос на неверифицированный номер телефона')
    def test_04(self):
        result = AuthMethods.forgot_password(not_verify_phone, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

    @allure.description('Запрос на несуществующий номер телефона')
    def test_05(self):
        result = AuthMethods.forgot_password('80000000000', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Невалидный номер телефона')
    def test_06(self):
        result = AuthMethods.forgot_password('80000000000123', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_07(self):
        result = AuthMethods.forgot_password('', None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Неверный тип данных integer')
    def test_08(self):
        result = AuthMethods.forgot_password(89260000002, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)





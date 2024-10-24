import time

import allure

from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods


@allure.epic('Post_forgot_password Общие проверки')
class TestCommonCheck:

    # @allure.description('Запросить 10 кодов подтверждения за 1 час')
    # def test_01(self):
    #     for i in range(10):
    #         time.sleep(5)
    #         result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')
    #         print(result.text)
    #         Checking.check_statuscode(result, 200)
    #
    # @allure.description('Запросить 11 кодов подтверждения за 1 час')
    # def test_02(self):
    #     time.sleep(10805)
    #     for i in range(10):
    #         time.sleep(5)
    #         result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')
    #         print(result.text)
    #         Checking.check_statuscode(result, 200)
    #
    #     result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')
    #     print(result.text)
    #     Checking.check_statuscode(result, 422)

    @allure.description('Запрос кода подтверждения с валидными данными')
    def test_03(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Одновременно указана и почта и номер телефона')
    def test_04(self):
        time.sleep(62)
        result = AuthMethods.forgot_password('89260000002', 'pawel_test_1@rambler.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствует body')
    def test_05(self):
        time.sleep(62)
        result = AuthMethods.forgot_password_without_body()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Запросить новый код подтверждения до истечения старого')
    def test_06(self):

        """Запрос кода подтверждения"""
        # time.sleep(62)
        result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Запрос нового кода подтверждения"""
        time.sleep(5)
        result = AuthMethods.forgot_password(None, 'pawel_test_1@rambler.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

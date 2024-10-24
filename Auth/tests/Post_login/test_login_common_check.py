import json

import allure

from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods


@allure.epic('Post_reset_password/login бщие проверки')
class TestLoginCommonCheck:

    @allure.description('Пользователь верифицирован')
    def test_01(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            required_fields = {
                "access_token": "string",
                "refresh_token": "string",
                "token_type": "bearer"
            }

            for field in required_fields:
                assert field in data, f"Отсутствует обязательное поле: {field}"
                print(f'Поле {field} присутствует')

    @allure.description('Повторный вход без предварительного выхода')
    def test_02(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Авторизация с нового устройства')
    def test_03(self):
        result = AuthMethods.login(
            '11112', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Пользователь не верифицирован')
    def test_04(self):
        result = AuthMethods.login(
            '11113', 'username=bmk20284%40nowni.com&password=Ohranatruda%402'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

import json
import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables


@pytest.mark.Auth
@allure.epic('Post_reset_password/request_verify_code Создание кода для верификации')
class TestResetPasswordCommonCheck:

    @allure.description('Запрос с валидными данными')
    def test_01(self, create_and_delete_users):
        """Создание пользователя"""
        user_id = create_and_delete_users
        print(user_id)

        """Отправка запроса на получение кода верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code(user_id)
        print(result.text)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            for i, k in data.items():
                assert i == 'message', 'Отсутствует обязательное поле "message"'
                print('Поле "message" присутствует')

    @allure.description('Запрос нового кода с валидными данными после истечения срока действия полученного кода')
    def test_02(self, create_and_delete_users):
        """Создание пользователя"""
        user_id = create_and_delete_users

        """Отправка запроса на получение кода верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code(user_id)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Запрос нового кода с валидными данными до истечения срока действия полученного кода')
    def test_03(self, create_and_delete_users):
        """Создание пользователя"""
        user_id = create_and_delete_users

        """Отправка запроса на получение кода верификации"""
        result = AuthMethods.request_verify_code(user_id)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

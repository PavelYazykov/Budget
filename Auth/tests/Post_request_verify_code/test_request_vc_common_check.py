import json
import time

import allure

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

user_id = '590faefa-472e-448a-a608-dd0c63a23458'


@allure.epic('Post_reset_password/request_verify_code Создание кода для верификации')
class TestCommonCheck:

    @allure.description('Запрос с валидными данными')
    def test_01(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code(
            'email', user_id
        )

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
    def test_02(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code(
            'email', user_id
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Запрос нового кода с валидными данными до истечения срока действия полученного кода')
    def test_03(self):
        result = AuthMethods.request_verify_code(
            'email', user_id
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

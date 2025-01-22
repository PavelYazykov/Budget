import time

import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import allure
from common_methods.variables import AuthVariables
user_id_not_verify = AuthVariables.user_id_not_verify
user_id_verify = AuthVariables.user_id_verify
not_verify_user_phone = AuthVariables.not_verify_phone_user_id
verify_user_phone = AuthVariables.verify_user_phone


@pytest.mark.Auth
@allure.epic('Post_reset_password/request_verify_code Проверка поля verify_type')
class TestVerifyType:

    @allure.description('Существующее значение: ("email")')
    def test_01(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_not_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Существующее значение: ("phone")')
    def test_02(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('phone', not_verify_user_phone)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Уже верифицированный phone')
    def test_03(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('phone', verify_user_phone)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

    @allure.description('Уже верифицированный email')
    def test_04(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

    @allure.description('Несуществующее значение ("voice")')
    def test_05(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('voice', user_id_not_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('уcтое поле')
    def test_06(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('', user_id_not_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_07(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code_without_vt(user_id_not_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_08(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('null', user_id_not_verify)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

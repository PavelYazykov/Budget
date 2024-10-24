import time

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import allure
user_id_not_verify = '590faefa-472e-448a-a608-dd0c63a23458'
user_id_verify = '7741e39b-a66a-45f3-a465-f7ca8e7c7eab'
not_verify_user_phone = '590faefa-472e-448a-a608-dd0c63a23458'
verify_user_phone = '7741e39b-a66a-45f3-a465-f7ca8e7c7eab'


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

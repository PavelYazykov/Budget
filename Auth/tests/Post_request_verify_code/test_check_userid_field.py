import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

user_id_exist = '590faefa-472e-448a-a608-dd0c63a23458'
user_id_not_exist = '590faefa-472e-448a-a608-dd0c63a99999'


@allure.epic('Post_reset_password/request_verify_code Проверка поля user_id')
class TestCheckUserID:

    @allure.description('Существующий user_id')
    def test_01(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Несуществующий user_id')
    def test_02(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_not_exist)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Пуcтое поле')
    def test_03(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', '')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_04(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code_without_userid('email')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_05(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', 'null')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


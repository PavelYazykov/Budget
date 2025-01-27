import time
import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
user_id_not_exist = AuthVariables.user_id_not_exist


@pytest.mark.Auth
@allure.epic('Post_reset_password/request_verify_code Проверка поля user_id')
class TestRequestVerifyCodeUserID:

    @allure.description('Существующий user_id')
    def test_01(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Отправка запроса на получение кода верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code(user_id_exist)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Несуществующий user_id')
    def test_02(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code(user_id_not_exist)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Пуcтое поле')
    def test_03(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_04(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code_without_userid()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_05(self):
        time.sleep(61)
        result = AuthMethods.request_verify_code('null')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


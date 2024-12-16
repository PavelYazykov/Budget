import time

import allure

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2

from common_methods.variables import AuthVariables
user_id_not_exist = AuthVariables.user_id_not_exist
another_user_id = '061566ea-ac9e-477d-bbd2-6690f530e29d'  #  Сделать автоматическое создание пользователя
verify_id = AuthVariables.user_id_verify


@allure.epic('Post_reset_password/verify проверка поля verify_type')
class TestVerifyType:
    """Проверка поля verify_type"""

    @allure.description('Существующее значение verify_type: ("email")')
    def test_01(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify(user_id_exist, 'email', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

    @allure.description('несуществующее значение verify_type: ("voice")')
    def test_02(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify(user_id_exist, 'voice', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('verify_type: Пуcтое поле')
    def test_03(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify(user_id_exist, '', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('verify_type: Поле отсутствует')
    def test_04(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify_without_vt(user_id_exist, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('verify_type: Null')
    def test_05(self, create_and_delete_users):
        """Создание пользователя"""
        user_id_exist = create_and_delete_users

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify(user_id_exist, 'null', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

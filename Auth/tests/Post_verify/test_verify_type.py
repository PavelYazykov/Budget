import time

import allure

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2

user_id_exist = '590faefa-472e-448a-a608-dd0c63a23458'
user_id_not_exist = '590faefa-472e-448a-a608-dd0c63a99999'
another_user_id = '061566ea-ac9e-477d-bbd2-6690f530e29d'
verify_id = '7741e39b-a66a-45f3-a465-f7ca8e7c7eab'


@allure.epic('Post_reset_password/verify роверка поля verify_type')
class TestVerifyType:
    """Проверка поля verify_type"""

    @allure.description('Существующее значение verify_type: ("email")')
    def test_01(self):

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

        """Подключение к БД"""
        with allure.step('Подключение к БД Изменение статуса email на не верифицирован'):
            with psycopg2.connect(
                    host='82.97.248.83',
                    user='postgres',
                    password='postgres',
                    dbname='budget',
                    port=25432
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """UPDATE users SET is_email_verified=False WHERE id = '590faefa-472e-448a-a608-dd0c63a23458'"""
                )
                connection.commit()

    @allure.description('есуществующее значение verify_type: ("voice")')
    def test_02(self):

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
    def test_03(self):

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
    def test_04(self):

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
    def test_05(self):

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

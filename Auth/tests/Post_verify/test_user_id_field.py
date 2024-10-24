import time

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2
import  allure
user_id_exist = '590faefa-472e-448a-a608-dd0c63a23458'
user_id_not_exist = '590faefa-472e-448a-a608-dd0c63a99999'
another_user_id = '061566ea-ac9e-477d-bbd2-6690f530e29d'


@allure.epic('Post_reset_password/verify Проверка поля user_id')
class TestUserIdField:

    @allure.description('Существующий user_id ( неверифицирован)')
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

    @allure.description('Чужой user_id')
    def test_02(self):

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify(another_user_id, 'email', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 404)

    @allure.description('Пуcтое поле')
    def test_03(self):

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify('', 'email', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Поле отсутствует')
    def test_04(self):

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify_without_userid('email', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Null')
    def test_05(self):

        """Запрос кода для верификации"""
        time.sleep(61)
        result = AuthMethods.request_verify_code('email', user_id_exist)
        Checking.check_statuscode(result, 200)

        """Получение кода"""
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.verify('null', 'email', result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)



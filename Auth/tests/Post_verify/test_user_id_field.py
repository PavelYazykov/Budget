import time
import random
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2
import allure
from common_methods.variables import AuthVariables
user_id_exist = AuthVariables.user_id_verify
email = str(random.randint(1111111111, 9999999999)) + '@mail.ru'
phone = '8' + str(random.randint(1111111111, 9999999999))
password = AuthVariables.password
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@allure.epic('Post_reset_password/verify Проверка поля user_id')
class TestUserIdField:

    @allure.description('Существующий user_id (неверифицирован)')
    def test_01(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify(user_id, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Чужой user_id')
    def test_02(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify(user_id_exist, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 404)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Пуcтое поле')
    def test_03(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify('', result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Поле отсутствует')  # 404 код
    def test_04(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify_without_userid(result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Null')
    def test_05(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify('null', result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

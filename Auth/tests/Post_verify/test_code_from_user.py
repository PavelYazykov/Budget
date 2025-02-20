import time
import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2
from common_methods.variables import AuthVariables
from faker import Faker
import random
fake = Faker()
email = str(random.randint(1111111111, 9999999999)) + '@mail.ru'
phone = '8' + str(random.randint(1111111111, 9999999999))
password = AuthVariables.password
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@allure.epic('Post_reset_password/verify Проверка поля code_from_user')
class TestCodeFromUser:

    @allure.description('Действующий код')
    def test_01(self):
        time.sleep(61)
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
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

    @allure.description('Несуществующий код')
    def test_02(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Проверка кода"""
            result_check = AuthMethods.verify(user_id, '000000')

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 400)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Истекший код')
    def test_03(self):
        """Создание пользователя"""
        time.sleep(301)
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Запрос кода для верификации"""
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            time.sleep(62)
            result_check = AuthMethods.verify(user_id, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 404)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('5 символов ')
    def test_04(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Ввод невалидного кода для верификации"""
            result_check = AuthMethods.verify(user_id, '12345')

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('7 символов ')
    def test_05(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Ввод невалидного кода для верификации"""
            result_check = AuthMethods.verify(user_id, '1234567')

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Пуcтое поле')
    def test_06(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Ввод невалидного кода для верификации"""
            result_check = AuthMethods.verify(user_id, '')

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Поле отсутствует')
    def test_07(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Ввод невалидного кода для верификации"""
            result_check = AuthMethods.verify_without_code(user_id)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Null')
    def test_08(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        try:
            """Ввод невалидного кода для верификации"""
            result_check = AuthMethods.verify(user_id, 'null')

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

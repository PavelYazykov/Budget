import time
import random
import pytest
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import allure
from common_methods.variables import AuthVariables
email = str(random.randint(1111111111, 9999999999)) + '@mail.ru'
phone = '8' + str(random.randint(1111111111, 9999999999))
password = AuthVariables.password
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@pytest.mark.verify_user_id
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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Чужой user_id')
    def test_02(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data_2, user_id_2 = AuthMethods.get_id(result_create_second_user)
        try:
            """Запрос кода для верификации"""
            time.sleep(301)
            result = AuthMethods.request_verify_code(user_id)
            Checking.check_statuscode(result, 200)

            """Получение кода"""
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.verify(user_id_2, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователей из БД"""
            AuthMethods.delete_user(user_id)
            AuthMethods.delete_user(user_id_2)

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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

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
            Checking.check_statuscode(result_check, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

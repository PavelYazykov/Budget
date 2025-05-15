import allure
import pytest

from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
import time
from common_methods.variables import AuthVariables
verify_phone = AuthVariables.phone
verify_email = AuthVariables.email
not_verify_email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
not_verify_phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@pytest.mark.forgot_password_email_field
@allure.epic('Post_forgot_password Проверка поля email')
class TestForgotPasswordEmailField:

    @allure.description('Проверка поля email - Запрос на верифицированную почту')
    def test_01(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(verify_email)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля email - Поле отсутствует')
    def test_02(self):
        time.sleep(62)
        result = AuthMethods.forgot_password_without_body()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Null')
    def test_03(self):
        time.sleep(62)
        result = AuthMethods.forgot_password(None)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Запрос на неверифицированную почту')
    def test_04(self):
        """Создание пользователя"""
        create_result = AuthMethods.registration(
            not_verify_email, password, last_name, first_name, middle_name, not_verify_phone, date_of_birth
        )
        Checking.check_statuscode(create_result, 201)
        data, user_id = AuthMethods.get_id(create_result)
        time.sleep(20)
        try:
            """Запрос кода"""
            result = AuthMethods.forgot_password(not_verify_email)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 403)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email- Запрос на несуществующую почту')
    def test_05(self):
        result = AuthMethods.forgot_password('qwertyzxcvbasdfg123@gmail.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля email - Невалидная почта')
    def test_06(self):
        result = AuthMethods.forgot_password('qwertyu.ru')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля email - Пустое поле')
    def test_07(self):
        result = AuthMethods.forgot_password('')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)



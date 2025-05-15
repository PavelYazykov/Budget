import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from Auth.methods.payloads import Payloads
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@pytest.mark.registr_phone
@allure.epic('Post/registration Проверка поля phone')
class TestRegistrationPhoneField:

    @allure.description('Проверка поля phone - 11 символов')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, '89770000000', date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, '89770000000', date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, '89770000000', email, date_of_birth
            )
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля phone - Null')  # Проверить по свагеру статус код
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, None, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data, user_id = AuthMethods.get_id(result)

        """Проверка наличия обязательных полей в ответе"""
        try:
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, None, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, None, email, date_of_birth
            )
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля phone - 10 символов')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, '8977000000', date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - 12 символов')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, '897700000000', date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Буквы')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, 'asdfghjkzxc', date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Спецсимволы')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, '@#$%^&@#$%^', date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Пустое поле')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, '', date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля phone - Неверный тип данных (integer)')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, 82345678901, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            data, user_id = AuthMethods.get_id(result)
            AuthMethods.delete_user(user_id)
        Checking.check_statuscode(result, 422)

import time
import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password
phone = AuthVariables.phone


@pytest.mark.Auth
@pytest.mark.reset_password_field_password
@allure.epic('Post/reset_password Проверка поля password')
class TestResetPasswordCheckPassword:

    @allure.description('Проверка поля password - 12 символов')
    def test_01(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(email, 'Aa1!tyhgvooa')
            Checking.check_statuscode(result_change, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - 100 символов')
    def test_02(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa'
                             '1@111111Aa1@111111Aa1@111111'
            )
            Checking.check_statuscode(result_change, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Пробел')
    def test_03(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Zx@1 kjgtreqpbd'
            )
            Checking.check_statuscode(result_change, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Ввод предыдущего пароля')
    def test_04(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Zx@1 kjgtreqpbd'
            )
            Checking.check_statuscode(result_change, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - 11 символов')
    def test_05(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Zx@1vbytrew'
            )
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - 101 символов')
    def test_06(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1'
                             '@111111Aa1@111111Aa1@1111112'
            )
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Пустое поле')
    def test_07(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, ''
            )
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Null')
    def test_08(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
               email, None
            )
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Пароль не соответствует требованиям')
    def test_09(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""

            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'zxcvbnmghqwertyu'
            )
            Checking.check_statuscode(result_change, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Неверный тип данных (integer)')
    def test_10(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 123456789963852741
            )
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Поле отсутствует')
    def test_11(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password_without_password(email)
            Checking.check_statuscode(result_change, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля password - Скомпрометированный пароль')
    def test_12(self):
        """Создание пользователя"""
        time.sleep(301)
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Запрос кода"""
            result = AuthMethods.forgot_password(email)
            Checking.check_statuscode(result, 200)
            result_code = AuthMethods.get_verify_code(result)

            """Проверка кода"""
            result_check = AuthMethods.code_check(email, result_code)

            """Проверка статус кода"""
            Checking.check_statuscode(result_check, 200)

            """Изменение пароля"""
            result_change = AuthMethods.reset_password(
                email, 'qwertyuiopA@123'
            )
            Checking.check_statuscode(result_change, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

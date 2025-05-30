import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
from Auth.methods.payloads import Payloads
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth


@pytest.mark.Auth
@pytest.mark.registr_common
@allure.epic('Post/registration - Общие проверки')
class TestRegistrationCommonCheck:

    @allure.description('Регистрация пользователя с валидными данными')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        user_id = None

        try:

            """Проверка наличия обязательных полей в ответе"""
            data = Checking.get_data(result)
            user_id = data['id']
            AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, last_name, first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Запрос без body')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration_without_body()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)



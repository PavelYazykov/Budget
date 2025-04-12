import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
password = AuthVariables.password


@pytest.mark.Auth
@allure.epic('Post_change_password Общие проверки')
class TestCommonCheck:

    @allure.description('Изменение пароля с валидными данными')
    def test_01(self):
        """Создание пользователя"""
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

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на изменение пароля"""
            result_change = AuthMethods.change_password(
                password, 'Ohranatruda@5', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Измененеие на текущий пароль')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение пароля"""
        result_change = AuthMethods.change_password(
            password, password, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)

    @allure.description('Запрос со старым access_token')
    def test_03(self):
        """Запрос со старым access_token"""
        pass  # Доделать!

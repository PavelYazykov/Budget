import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.Users
@allure.epic('Patch/users/me Изменение информации текущий пользователь')
class TestPatchUsersCommon:

    @allure.description('Изменение информации о пользователе с валидными данными')
    def test_01(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                AuthVariables.email_for_create_user_2, AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user_2, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значений обязательных полей"""
            UserResponse.check_required_fields_value(
                result, AuthVariables.email_for_create_user_2, AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user_2, AuthVariables.date_of_birth
            )
        finally:
            AuthMethods.delete_user(user_id)





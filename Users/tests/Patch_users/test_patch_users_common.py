import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import CommonVariables, AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Изменение информации текущий пользователь')
class TestPatchUsersCommon:

    @allure.description('Изменение информации о пользователе с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значений обязательных полей"""
            UserResponse.check_required_fields_value(
                result, AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
            )
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')




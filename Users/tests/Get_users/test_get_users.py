import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import CommonVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.Users
@allure.epic('Get/users/me Получение информации о текущем пользователе')
class TestGetUsers:

    @allure.description('Получение информации о текущем пользователе (авторизованной пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о пользователе"""
        result = UsersMethods.get_user(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('Получение информации о текущем пользователе (неавторизованной пользователь)')
    def test_02(self):

        """Запрос информации о пользователе"""
        result = UsersMethods.get_user_without_auth()
        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)





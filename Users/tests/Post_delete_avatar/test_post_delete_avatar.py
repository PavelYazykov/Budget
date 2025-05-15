import time

import allure
import pytest

from common_methods.checking import Checking
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.Users
@pytest.mark.Users_delete_avatar
@allure.epic('Post/users/delete_avatar Удаление аватара')
class TestPostDeleteAvatar:

    @allure.description('Удалить существующий аватар')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbJPG.jpg', '../../download_files/1mbJPG.jpg', access_token
        )
        Checking.check_statuscode(result, 200)

        """Удаление аватара"""
        result = UsersMethods.delete_avatar(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('Удалить несуществующий аватар')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление аватара"""
        result = UsersMethods.delete_avatar(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

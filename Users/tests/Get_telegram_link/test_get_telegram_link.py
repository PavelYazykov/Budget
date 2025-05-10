import allure
import pytest

from Users.methods.users_methods import UsersMethods
from common_methods.checking import Checking


@pytest.mark.Users
@allure.epic(
    'Get/users/get_telegram_link - ссылка на телеграм-бота, напоминающего пользователю о предстоящих платежах'
)
class TestGetTelegramLink:

    @allure.description('get_telegram_link - Запрос ссылки авторизованный пользователь')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос ссылки"""
        result = UsersMethods.get_telegram_link(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия ссылки"""
        data = Checking.get_data(result)
        assert 'telegram_link' in data

    @allure.description('get_telegram_link - Запрос ссылки авторизованный пользователь')
    def test_02(self):
        """Запрос ссылки"""
        result = UsersMethods.get_telegram_link_without_access_token()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)



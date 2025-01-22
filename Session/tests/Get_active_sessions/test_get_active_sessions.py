import allure
import pytest

from common_methods.checking import Checking
from Session.methods.sessions_methods import SessionsMethods
from Session.methods.payloads import SessionPayloads


@pytest.mark.Session
@allure.epic('Get/active_sessions/ Получение списка активных сессий пользователя')
class TestGetActiveSessions:

    @allure.description('Запрос сессий пользователя (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос сессий"""
        result = SessionsMethods.get_active_sessions(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        print(result.json())

        """Проверка обязательных полей"""
        SessionPayloads.check_required_fields(result, SessionPayloads.get_payloads)

    @allure.description('Запрос сессий пользователя (неавторизованный пользователь)')
    def test_02(self):

        """Запрос сессий"""
        result = SessionsMethods.get_active_sessions_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

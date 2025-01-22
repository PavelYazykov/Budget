import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads
from common_methods.variables import AuthVariables


@pytest.mark.Settings
@allure.epic('Post/api/v1/settings/contact_to_admin/ Связь с администратором общие проверки')
class TestContactAdminCommon:

    @allure.description('Связь с администратором - Создание запроса с валидными данными (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            AuthVariables.email, 'message topic', SettingsPayloads.message,
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('Связь с администратором - Создание запроса (неавторизованный пользователь)')
    def test_02(self):

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message topic', SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('Связь с администратором - Body отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@pytest.mark.Settings
@allure.epic('Get/api/v1/settings/my/ Настройки авторизованного пользователя')
class TestGetSettings:

    @allure.description('Запрос настроек (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос настроек пользователя"""
        result = SettingsMethods.get_settings(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

    @allure.description('Запрос настроек (неавторизованный пользователь)')
    def test_02(self):
        """Запрос настроек пользователя"""
        result = SettingsMethods.get_settings_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)
        
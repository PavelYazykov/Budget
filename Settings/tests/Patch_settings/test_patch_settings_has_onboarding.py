import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking


@pytest.mark.Settings
@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля has_onboarding')
class TestPatchSettingsHasOnboarding:

    @allure.description('поле has_onboarding - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_onboarding(True, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['has_onboarding'] is True

    @allure.description('поле has_onboarding - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_onboarding(False, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['has_onboarding'] is False
import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - общие проверки')
class TestPatchSettingsCommon:

    @allure.description('Body отсутствует')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение настроек"""
        result = SettingsMethods.patch_settings_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Одновременно установить персональный и бизнес аккаунт')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение настроек"""
        result = SettingsMethods.patch_settings(
           True, True, True, True, True,
            True, True, 2, None, access_token
        )
        print(result.text)

        # """Проверка статус кода"""
        # Checking.check_statuscode(result, 422)



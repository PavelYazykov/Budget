import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля telegram_notifications')
class TestPatchSettingsTelegramNotifications:

    @allure.description('поле telegram_notifications - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля telegram_notifications"""
        data = Checking.get_data(result)
        assert data['data']['telegram_notifications'] is True

    @allure.description('поле telegram_notifications - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            False, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля telegram_notifications"""
        data = Checking.get_data(result)
        assert data['data']['telegram_notifications'] is False

    @allure.description('поле telegram_notifications - значение Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            None, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля telegram_notifications"""
        data = Checking.get_data(result)
        assert data['data']['telegram_notifications'] is None

    @allure.description('поле telegram_notifications - Неверный тип данных integer')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            12345, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_notifications - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            '12345', True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_notifications - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, None,
            '', True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_notifications - Поле отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля telegram_notifications"""
        data = Checking.get_data(result)
        assert data['data']['telegram_notifications'] is True

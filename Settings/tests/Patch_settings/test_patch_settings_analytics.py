import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля analytics')
class TestPatchSettingsAnalytics:

    @allure.description('поле analytics - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['analytics'] is True

    @allure.description('поле analytics - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, False, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['analytics'] is False

    @allure.description('поле analytics - значение Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, None, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле analytics - Неверный тип данных integer')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, 12345, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле analytics - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, 'None', True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле analytics - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            True, False, '', True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле analytics - Пустое отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_analytics(
            True, False, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)



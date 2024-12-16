import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля personal_accounting')
class TestPatchSettingsPersonalAccount:

    @allure.description('поле personal_accounting - значение True')
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
        assert data['data']['personal_accounting'] is True

    @allure.description('поле personal_accounting - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['personal_accounting'] is False

    @allure.description('поле personal_accounting - значение Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            None, False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле personal_accounting - Неверный тип данных integer')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            12345, False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле personal_accounting - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            'None', False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле personal_accounting - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            '', False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле personal_accounting - Пустое отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_personal_accounting(
            False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)



import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@pytest.mark.Settings
@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля push_notifications')
class TestPatchSettingsPushNotifications:

    @allure.description('поле push_notifications - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля push_notifications"""
        data = Checking.get_data(result)
        assert data['data']['push_notifications'] is True

    @allure.description('поле push_notifications - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            False, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля push_notifications"""
        data = Checking.get_data(result)
        assert data['data']['push_notifications'] is False

    @allure.description('поле push_notifications - значение Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            None, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле push_notifications - Неверный тип данных integer')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            123456, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле push_notifications - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            'string', True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле push_notifications - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            '', True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле push_notifications - Пустое отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_push_notifications(
            False, True, True, True, True,
            True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)



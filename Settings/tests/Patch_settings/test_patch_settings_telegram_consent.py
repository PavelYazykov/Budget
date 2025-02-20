import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking


@pytest.mark.Settings
@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля telegram_consent')
class TestPatchSettingsTelegramConsent:

    @allure.description('поле telegram_consent - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, [1],
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля telegram_consent"""
        data = Checking.get_data(result)
        assert data['data']['telegram_consent'] is True

    @allure.description('поле telegram_consent - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, [1],
            True, False, False, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля telegram_consent"""
        data = Checking.get_data(result)
        assert data['data']['telegram_consent'] is False

    @allure.description('поле telegram_consent - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_push_notifications(
            False, True, True, True, True,
            True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('поле telegram_consent - значение Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, True, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_consent - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, True, 123, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_consent - Неверный тип данных string')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, True, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле telegram_consent - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, True, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


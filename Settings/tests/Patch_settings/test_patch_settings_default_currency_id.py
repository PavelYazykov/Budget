import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@pytest.mark.Settings
@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля default_currency_id')
class TestPatchSettingsDefaultCurrencyId:

    @allure.description('поле default_currency_id - Существующее значение')
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

        """Проверка значения поля default_currency_id"""
        data = Checking.get_data(result)
        assert data['data']['default_currency_id'] == 2

    @allure.description('поле default_currency_id - Null')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, None, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле default_currency_id - Несуществующее значение')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 10, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('поле default_currency_id - Значение 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 0, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле default_currency_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, -2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле default_currency_id - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, '', None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле default_currency_id - Поле отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_default_currency_id(
            False, True, True, True, True,
            True, True, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('поле default_currency_id - Неверный тип данных string')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 'nnnn', None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

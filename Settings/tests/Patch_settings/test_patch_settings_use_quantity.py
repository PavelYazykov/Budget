import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля use_quantity')
class TestPatchSettingsUseQuantity:

    @allure.description('поле use_quantity - значение True')
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

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля use_quantity"""
        data = Checking.get_data(result)
        assert data['data']['use_quantity'] is True

    @allure.description('поле use_quantity - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, False,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        SettingsPayloads.check_required_fields(result, SettingsPayloads.required_fields)

        """Проверка значения поля use_quantity"""
        data = Checking.get_data(result)
        assert data['data']['use_quantity'] is False

    @allure.description('поле use_quantity - значение Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, None,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле use_quantity - Неверный тип данных integer')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, 123456,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле use_quantity - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, 'string',
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле use_quantity - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, '',
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле use_quantity - Пустое отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_use_quantity(
            False, True, True, True,
            True, True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)



import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking


@pytest.mark.Settings
@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля remind_in_days')
class TestPatchSettingsRemindDays:

    @allure.description('поле remind_in_days - значение integer')
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

        """Проверка значения поля remind_in_days"""
        data = Checking.get_data(result)
        assert data['data']['remind_in_days'] == [1]

    @allure.description('поле remind_in_days - значение массив целых чисел')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, [1, 3],
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля remind_in_days"""
        data = Checking.get_data(result)
        assert data['data']['remind_in_days'] == [1, 3]

    @allure.description('поле remind_in_days - Null')
    def test_03(self, auth_fixture):
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

        """Проверка значения поля remind_in_days"""
        data = Checking.get_data(result)
        assert data['data']['remind_in_days'] is None

    @allure.description('поле remind_in_days - Null')
    def test_04(self, auth_fixture):
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

        """Проверка значения поля remind_in_days"""
        data = Checking.get_data(result)
        assert data['data']['remind_in_days'] is None

    @allure.description('поле push_notifications - Пустое отсутствует')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_push_notifications(
            False, True, True, True, True,
            True, 2, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('поле remind_in_days - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, '',
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле remind_in_days - Значене  = 0')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 0,
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле remind_in_days - Отрицательное значение')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, -1,
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле remind_in_days - Неверный тип данных string')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 'string',
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)






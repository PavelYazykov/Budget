import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля registration_consent')
class TestPatchSettingsRegistrationConsent:

    @allure.description('поле registration_consent - значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, True, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля registration_consent"""
        data = Checking.get_data(result)
        assert data['data']['registration_consent'] is True

    @allure.description('поле registration_consent - значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, False, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля registration_consent"""
        data = Checking.get_data(result)
        assert data['data']['registration_consent'] is False

    @allure.description('поле push_notifications - Пустое отсутствует')
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

    @allure.description('поле registration_consent - значение Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, None, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля registration_consent"""
        data = Checking.get_data(result)
        assert data['data']['registration_consent'] is None

    @allure.description('поле registration_consent - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, 123, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле registration_consent - Неверный тип данных string')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, 'string', True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле registration_consent - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_2(
            False, True, True, True, True,
            True, True, 2, None, 1,
            True, '', True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


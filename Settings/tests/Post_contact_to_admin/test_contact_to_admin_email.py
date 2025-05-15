import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads
from common_methods.variables import AuthVariables


@pytest.mark.Settings
@allure.epic('Post/api/v1/settings/contact_to_admin/ Связь с администратором проверка поля email')
class TestContactAdminEmail:

    @allure.description('Связь с администратором - Существующий email')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            AuthVariables.email, 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('Связь с администратором - несуществующий в БД email')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            'email_951753@mail.ru', 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('Связь с администратором - несуществующий email')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            'email_951753mail.ru', 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Связь с администратором - Пустое поле')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            '', 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Связь с администратором - Поле отсутствует')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin_without_email(
            'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Связь с администратором - Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            None, 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Связь с администратором - Неверный тип данных integer')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос администратору"""
        result = SettingsMethods.post_contact_to_admin(
            123456789, 'message topic', SettingsPayloads.message, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
